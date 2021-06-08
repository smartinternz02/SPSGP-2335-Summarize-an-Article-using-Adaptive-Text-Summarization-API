# Example directly sending a text string:

import requests
r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': 'YOUR_TEXT_HERE',
    },
    headers={'api-key': '79728e79-d56e-40bc-be98-ece560a7dd3c'}
)
print(r.json())