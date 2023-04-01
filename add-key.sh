#!/bin/bash

# Prompt the user for the OpenAI API key
read -p "Enter your OpenAI API key: " openai_key

# Export the OpenAI API key
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    export OPENAI_API_KEY="$openai_key"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    export OPENAI_API_KEY="$openai_key"
elif [[ "$OSTYPE" == "msys" ]]; then
    set OPENAI_API_KEY="$openai_key"
fi

echo "OpenAI API key set temporarily."