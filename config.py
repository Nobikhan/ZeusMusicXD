from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "13457338"))
API_HASH = getenv("API_HASH", "165a136cf6a98292c06a28451b756d2a")
BOT_TOKEN = getenv("BOT_TOKEN","5255059821:AAFrew0wbWQM9jSTRyg-dpCjOIC_rGQ-m8I")
BOT_NAME = getenv("BOT_NAME","Ayano_Robot_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "AQA3MImHGjK0DhlQgZPZ75_0b_IX5Q1ceTSycQQ8O1Fkk-7L56Y0CUjfLpC-iil0mnATPcO9CcZ6SA1I6_qBeTHM9j-PlDLiJR0_GRzksRfguKrUT-FMDT56lboTXnefbu3x2SualdQm3ihaPRF4w321PWcCzhH1zgTSDEsIAP-n0q01jHp-vpbnV1GhXmGWszrrr9wyV_NXsnICekvfA9ZP5KeenNp8sECIrVbnP5ocZk8enfh9XV7pjBUdm0uqK8e5nOqPG6ZfbFUQhWfFehSkEXYawcQmNhTcKApgtva_LFs0sa1L-o6wCRAVvxrJXyF6uE7SU7zJbPipsf47Vj0qAAAAAThadzEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5269906172 5016880247").split()))
