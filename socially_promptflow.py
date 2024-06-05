import json
from promptflow.core import tool
from promptflow.core import Prompty
from promptflow.client import PFClient
from promptflow.tracing import start_trace

from pathlib import Path
folder = Path(__file__).parent.absolute().as_posix()

# start a trace session, and print a url for user to check trace
start_trace()

@tool
def flow_entry(    
      blog_title: any,
      blog_link: any,
      call_to_action: any,
      post_type: any
) -> str:
  # path to prompty (requires absolute path for deployment)
  path_to_prompty = folder + "/socially.prompty"

  # load prompty as a flow
  flow = Prompty.load(path_to_prompty)
 
  # execute the flow as function
  result = flow(
    blog_title = blog_title,
    blog_link = blog_link,
    call_to_action = call_to_action,
    post_type = post_type
  )

  return result

if __name__ == "__main__":
   json_input = '''{
  "blog_title": "LLM based development tools - PromptFlow vs LangChain vs Semantic Kernel",
  "blog_link": "https://techcommunity.microsoft.com/t5/educator-developer-blog/llm-based-development-tools-promptflow-vs-langchain-vs-semantic/ba-p/4149252",
  "call_to_action": "GitHub Sample Code at https://github.com/BethanyJep/Swahili-Tutor",
  "post_type": "Twitter"
}'''
   args = json.loads(json_input)

   result = flow_entry(**args)
   print(result)
