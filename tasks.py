# Two tasks need to be created as we have two agents

from crewai import Task
from tools import tool
from agents import blog_researcher,blog_writer

#Research task
research_task = Task(
    description=(
        'Idetify the video {topic}.'
        'Get detailed information about the video from the channel.'
        ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of the video content.',
    tools=[yt_tool],
    agent=blog_researcher
)

#Blog Writing Task
writing_task = Task(
    description=(
        'Get the information from the yt channel video on the topic {topic}.'
        ),
    expected_output='Summarize the information from the video o the topic{topic} annd create the content for the blog.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)

