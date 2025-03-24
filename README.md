# Multi-Agent-SEO-Blog-Generator

The Python-based multi-agent system consists of the following agents:

1. Research Agent: Finds trending HR topics using the LLM (openai’s gpt-4o-mini used as an example).
2. Content Planning Agent: Generates a structured outline based on the chosen topic.
3. Content Generation Agent: Writes a 2000-word blog using the generated outline.
4. SEO Optimization Agent: Enhances the content for SEO optimization and readability.
5. Review Agent: Proofreads and humanizes the text to ensure quality

Final Output → The blog is saved to a .txt file

Tools and Frameworks Used

Python 3.10+: For running the system.
LangChain: To build and manage the LLM-based agents.
OpenAI GPT (gpt-4o-mini): Used as the primary LLM for generation.
getpass: For securely entering API keys.
os: For environment variable management.

Installation Steps

1.Clone the Repository:

 git clone <repository_url>
 cd <repository_folder>

2.Create a Virtual Environment:

 python -m venv env
 source env\Scripts\activate

3.Install Dependencies:

 pip install -r requirements.txt

4.Add Your API Key, or alternatively, the program will prompt you to enter it during runtime.

5.Run the Script:

python blog_generator.py

