#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getpass
import os
#Load the LLM using API key - (eg:OpenAI)
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

llm = init_chat_model("gpt-4o-mini", model_provider="openai")


# In[1]:


#Research Agent
class ResearchAgent:
    def find_trending_topic(self):
        query = "What are the top trending HR topics in 2025?"
        response = llm.generate([query])
        return response.generations[0].text.strip()


# In[ ]:


#Content Planning Agent
class ContentPlanningAgent:
    def create_outline(self, topic):
        query = f"Create a detailed blog outline for the topic: {topic}"
        response = llm.generate([query])
        return response.generations[0].text.strip()


# In[ ]:


#Content Generation Agent
class ContentGenerationAgent:
    def generate_blog(self, outline):
        query = f"Write a 2000-word blog based on the following outline: {outline}"
        response = llm.generate([query])
        return response.generations[0].text.strip()


# In[ ]:


#SEO Optimization Agent
class SEOOptimizationAgent:
    def optimize_content(self, content):
        query = f"Optimize the following blog for SEO with keywords and readability improvements: {content}"
        response = llm.generate([query])
        return response.generations[0].text.strip()


# In[ ]:


#Review Agent
class ReviewAgent:
    def review_blog(self, content):
        query = f"Proofread this blog and humanize it: {content}"
        response = llm.generate([query])
        return response.generations[0].text.strip()


# In[ ]:


#Main function containing calls to each agent
def main():
    research_agent = ResearchAgent()
    planning_agent = ContentPlanningAgent()
    generation_agent = ContentGenerationAgent()
    seo_agent = SEOOptimizationAgent()
    review_agent = ReviewAgent()

    print("Researching trending topics...")
    topic = research_agent.find_trending_topic()
    print(f"Topic Found: {topic}\n")

    print("Creating blog outline...")
    outline = planning_agent.create_outline(topic)
    print(f"Outline Created:\n{outline}\n")

    print("Generating blog content...")
    blog_content = generation_agent.generate_blog(outline)

    print("Optimizing content for SEO...")
    optimized_content = seo_agent.optimize_content(blog_content)

    print("Reviewing and refining blog...")
    final_content = review_agent.review_blog(optimized_content)

    print("Blog Generation Complete.\n")
    with open('generated_blog.txt', 'w') as f: #to save the generated blog in a .txt file
        f.write(final_content)

if __name__ == "__main__":
    main()

