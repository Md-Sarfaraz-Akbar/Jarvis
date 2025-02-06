# Jarvis

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-orange)

Jarvis is an AI-powered assistant that uses OpenAI's GPT-3.5-turbo model to generate responses based on user input.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Setup

### Prerequisites

- Python 3.6 or higher
- An OpenAI API key

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Md-Sarfaraz-Akbar/Jarvis.git
    cd Jarvis
    ```

2. **Install the required dependencies:**
    ```bash
    pip install openai
    ```

3. **Configure your OpenAI API key:**
    - Open `config.py` and replace `"your_openai_api_key_here"` with your actual OpenAI API key.

## Usage

Run the main script to interact with Jarvis:
```bash
python main.py
```

## Example

The following example demonstrates how to use Jarvis to generate an email for resignation:

```python
import openai
from config import apikey

client = openai.OpenAI(api_key=apikey)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write an email to my boss for resignation?"}
    ],
    temperature=0.7,
    max_tokens=256
)

print(response.choices[0].message.content)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
