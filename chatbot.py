from dotenv import load_dotenv
from anthropic import Anthropic
from rich.console import Console
from rich.panel import Panel

load_dotenv()
client = Anthropic()
console = Console()
model = "claude-sonnet-5-5"
TOKEN_LIMIT = 1500


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system:
        params["system"] = system

    console.print("[bold cyan]Assistant:[/] ", end="")

    with client.messages.stream(**params) as stream:
        for text in stream.text_stream:
            console.print(text, end="", markup=False, highlight=False)
        message = stream.get_final_message()

    console.print()
    reply = "".join(b.text for b in message.content if b.type == "text")
    return reply, message.usage


system_prompt = """The user is learning AI and wants a fun chat partner.
Talk like a laid-back, witty friend: casual slang, playful roasting,
sarcastic jokes, but always give a correct, helpful answer underneath
the humor. Keep replies short."""

messages = []
total_tokens = 0

console.print(Panel(
    "[bold magenta]😎 Funny Chatbot[/]\n[dim]Type 'quit' or 'exit' to leave[/]",
    expand=False,
))

while True:
    if total_tokens > TOKEN_LIMIT:
        console.print("[bold red]Token limit reached. Start a new session.[/]")
        break

    user_input = console.input("\n[bold green]You:[/] ").strip()
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit"]:
        console.print("[bold yellow]Bye! 👋[/]")
        break

    add_user_message(messages, user_input)
    answer, usage = chat(messages, system=system_prompt)
    add_assistant_message(messages, answer)

    total_tokens += usage.input_tokens + usage.output_tokens
    console.print(f"[dim]Tokens used: {total_tokens} / {TOKEN_LIMIT}[/]")
    console.rule(style="dim")