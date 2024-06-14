from internetspeed import InternetSpeedTwitterBot
import os,dotenv

dotenv.load_dotenv()

i_speed=InternetSpeedTwitterBot()

i_speed.get_internet_speed()

if i_speed.down<os.getenv('PROMISE_DOWN') or i_speed.up<os.getenv('PROMISE_UP'):
    i_speed.tweet_at_provider()