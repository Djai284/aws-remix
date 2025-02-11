import os
from google import genai
import json
import yaml


def read_file_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            try:  # Attempt JSON parsing
                content = json.load(file)
                file_type = "json"
                return content, file_type
            except json.JSONDecodeError:
                pass  # Not JSON, try YAML

            try:  # Attempt YAML parsing
                file.seek(0)  # Reset file pointer
                content = yaml.safe_load(file)
                file_type = "yaml"
                return content, file_type
            except yaml.YAMLError:
                pass  # Not YAML, treat as plain text

            file.seek(0)  # Reset file pointer
            content = file.read()
            file_type = "text"  # Default to text
            return content, file_type

    except FileNotFoundError:
        return "File not found.", None
    except Exception as e:
        return f"Error reading file: {e}", None


def summarize_text(prompt, client, model_name="gemini-2.0-flash"):
    try:
        response = client.models.generate_content(model=model_name, contents=[prompt])
        return response.text
    except Exception as e:  # Catch any potential errors
        return f"API request error: {e}"


def create_prompt(file_content, file_type):
    """
    Create a prompt for the LLM that instructs it to generate a Markdown report.
    The report should include:
      1. A concise summary of the AWS account details.
      2. Recommended remediations and improvements organized by the AWS Well-Architected Framework (WAFR) pillars.
         For example: Security, Reliability, Performance Efficiency, Cost Optimization, and Operational Excellence.
      3. Clear headings, bullet points, and sections as needed.

    The AWS account data is provided below in either JSON, YAML, or plain text.
    """
    if file_type == "json":
        prompt = f"""
              You are a cloud architect. You have been provided with a JSON report that summarizes an AWS account.
              Your task is to produce a Markdown formatted report that includes:

              1. **Quick Summary of the AWS Account:**  
                - A brief overview of key details such as the account number, alias, active regions, and important cost/resource information.
                
              2. **Recommended Remediations:**  
                For each of the AWS Well-Architected Framework (WAFR) pillars, please provide recommended remediations and improvements.  
                The WAFR pillars to consider are:  
                - **Security**  
                - **Reliability**  
                - **Performance Efficiency**  
                - **Cost Optimization**  
                - **Operational Excellence**  

                For each pillar, include any relevant questions or areas of focus from the WAFR guidelines that the report data might help address, and list specific remediation recommendations (using bullet points).

              Please produce the final report entirely in Markdown. Use headings, subheadings, and bullet points as necessary.

              Below is the JSON data:

              ```json
              {json.dumps(file_content, indent=4)}
              ```
              """
    elif file_type == "yaml":
        prompt = f"""
              You are a cloud architect. You have been provided with a YAML report that summarizes an AWS account.
              Your task is to produce a Markdown formatted report that includes:

              1. **Quick Summary of the AWS Account:**  
                - A brief overview of key details such as the account number, alias, active regions, and important cost/resource information.
                
              2. **Recommended Remediations:**  
                For each of the AWS Well-Architected Framework (WAFR) pillars, please provide recommended remediations and improvements.  
                The WAFR pillars to consider are:  
                - **Security**  
                - **Reliability**  
                - **Performance Efficiency**  
                - **Cost Optimization**  
                - **Operational Excellence**  

                For each pillar, include any relevant questions or areas of focus from the WAFR guidelines that the report data might help address, and list specific remediation recommendations (using bullet points).

              Please produce the final report entirely in Markdown. Use headings, subheadings, and bullet points as necessary.

              Below is the YAML data:

              ```yaml
              {yaml.dump(file_content, default_flow_style=False)}
              ```
              """
    else:  # Plain text
        prompt = f"""
              You are a cloud architect. You have been provided with a text report that summarizes an AWS account.
              Your task is to produce a Markdown formatted report that includes:

              1. **Quick Summary of the AWS Account:**  
                - A brief overview of key details such as the account number, alias, active regions, and important cost/resource information.
                
              2. **Recommended Remediations:**  
                For each of the AWS Well-Architected Framework (WAFR) pillars, please provide recommended remediations and improvements.  
                The WAFR pillars to consider are:  
                - **Security**  
                - **Reliability**  
                - **Performance Efficiency**  
                - **Cost Optimization**  
                - **Operational Excellence**  

                For each pillar, include any relevant questions or areas of focus from the WAFR guidelines that the report data might help address, and list specific remediation recommendations (using bullet points).

              Please produce the final report entirely in Markdown. Use headings, subheadings, and bullet points as necessary.

              Below is the text data:

              ```
              {file_content}
              ```
              """
              
    return prompt

if __name__ == "__main__":
    filepath = input("Enter the file path: ")
    file_content, file_type = read_file_content(filepath)

    # Gemini API credentials
    API_KEY = "AIzaSyBiXu8ruLvn1LDUKfEBFj0PXA4f_qJGK7k"

    # Create a client object with the API key
    client = genai.Client(api_key=API_KEY)

    # Check if file_content indicates an error
    if isinstance(file_content, str) and "Error" in file_content:
        print(file_content)
    elif file_type is None:  # File not found
        print("File not found")
    else:
        prompt = create_prompt(file_content, file_type)
        summary = summarize_text(prompt, client)
        print(summary)
