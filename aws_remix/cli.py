import typer
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from aws_remix import summary, collector
from aws_remix.collector import cost  # to call cost.collect_cost_info

app = typer.Typer(help="AWS Remix: A CLI tool for summarizing your AWS account.")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()

@app.command()
def scan(
    output: str = typer.Option(
        "markdown",
        help="Output format: json, yaml, markdown, txt, readme"
    ),
    regions: str = typer.Option(
        "",
        help="Comma-separated list of AWS regions to scan. Leave blank to scan only relevant regions."
    ),
    all_regions: bool = typer.Option(
        False,
        help="If set, scan all active regions regardless of cost relevance."
    ),
    output_file: str = typer.Option(
        "",
        help="Path to output file. Supported file types: txt, readme, json, yaml. If not provided, the report is printed to the console."
    ),
    lens: str = typer.Option(
        "",
        help=(
            "Optionally specify a lens to focus the scan. Possible values: "
            "'security', 'cost', 'reliability', 'performance', 'operational', 'sustainability'. "
            "If omitted, collects all data."
        )
    )
):
    """
    Scan the AWS account and generate a summary report.
    """
    # If user provided a non-empty comma-separated list, use that.
    # Otherwise, if --all-regions is True, use all active regions.
    # Otherwise, if no regions specified, call the cost collector to get the relevant regions.
    if regions.strip():
        region_list = [r.strip() for r in regions.split(",")]
    elif all_regions:
        # Use all active regions (this might be a larger list)
        region_list = summary.get_all_active_regions()
    else:
        # Use cost collector to determine the relevant regions.
        cost_info = cost.collect_cost_info()
        relevant_regions = cost_info.get("RelevantRegions", [])
        if not relevant_regions:
            # Fall back to all active regions if cost info returns no relevant regions.
            region_list = summary.get_all_active_regions()
        else:
            region_list = relevant_regions

    lens_param = lens.lower().strip() if lens else None

    # Validate lens
    valid_lenses = {"security", "cost", "reliability", "performance", "operational", "sustainability"}
    if lens_param and lens_param not in valid_lenses:
        typer.echo(f"Unsupported lens: {lens_param}. Ignoring lens parameter.")
        lens_param = None

    console = Console()
    start_time = time.time()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        progress_task = progress.add_task("[bold green]Scanning AWS account...", total=100)
        # Pass the region_list (which is now either relevant regions or all regions) into the summary.
        report = summary.generate_full_summary(region_list, lens=lens_param, progress=progress)
        progress.update(progress_task, completed=100, description="[bold green]Scan complete")

    elapsed = time.time() - start_time
    formatted_report = summary.format_report(report, output)

    if output_file:
        try:
            with open(output_file, "w") as f:
                f.write(formatted_report)
            console.print(f"[bold green]Report written to {output_file} in {elapsed:.2f} seconds.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error writing to file: {e}[/bold red]")
    else:
        console.print(formatted_report)
        console.print(f"[bold green]Scan completed in {elapsed:.2f} seconds.[/bold green]")

if __name__ == "__main__":
    app()
