import dotenv
from pydantic_ai import Agent


dotenv.load_dotenv()

model = 'openai:o4-mini'
agent = Agent(
    model,
    system_prompt='Be concise, reply with one sentence.',
)

if __name__ == '__main__':
    result = agent.run_sync('Where does "hello world" come from?')
    print(result.output)
    print(result.usage())