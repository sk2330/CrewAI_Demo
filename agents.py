from crewai import Agent
from tools import yt_tool

## first agent- Creating Researcher for blog

blog_researcher=Agent(
    role='Blog researcher from Youtube Videos',
    goal='Get the content from relevent topic{topic} from the youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Data Science,AI, Machine Learning and Generative AI"
    )
    tools=[yt_tool],
    allow_delegation=True
)

# 2nd agent-creating a blog writer for the blog from the info got from researcher(1st agent)
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate tech stories  of the video{topic} from Youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics you craft"
        "engaging narratives that captivate and educate."
    )
    tools=[yt_tool],
    allow_delegation=False
)