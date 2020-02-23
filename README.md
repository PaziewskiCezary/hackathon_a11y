# hackathon_a11y

Authors: Ada Kochlewska, Zuzanna Lewandowska, Tomasz Necio, Cezary Paziewski, Anna Stróż

This is a prototype of a YouTube interface that can be controlled only with a single button. 
It can be used by severely disabled people who control too few muscle groups to use computer
in a normal way. Elements of the interface are highlighted sequentially and have audiodescriptions.

The project was developed during Hackathon+ 2019 in Warsaw.

![alt text](https://raw.githubusercontent.com/PaziewskiCezary/hackathon_a11y/master/basic_instinct.png)
![alt text](https://raw.githubusercontent.com/PaziewskiCezary/hackathon_a11y/master/basic_instinct_2.png)
![alt text](https://raw.githubusercontent.com/PaziewskiCezary/hackathon_a11y/master/sharon_stone.png)


## Installation

Requirements: Python 3.7+, VLC

```console
git clone https://github.com/PaziewskiCezary/hackathon_a11y
cd hackathon_a11y
echo 'YT_API_KEY = "Qwertyuiop123456"' > hackathon_a11y/api_key.py
pip3 install -r requirements.txt --user
python3 -m hackathon_a11y
```

(replace `Qwertyuiop123456` with an API key from https://developers.google.com/youtube/v3/getting-started)
