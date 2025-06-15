import logfire
import dotenv


dotenv.load_dotenv()

logfire.configure()
logfire.info('Hello, {place}!', place='World')
