# About
This tool will daily crawl https://arxiv.org and use LLMs to summarize them.

# How to use
This repo will daily crawl arXiv papers about **cs.CV, cs.GR**, and use **DeepSeek** to summarize the papers in **Chinese**.
If you wish to crawl other arXiv categories, use other LLMs or other languages, please follow the bellow instructions.
Otherwise, you can directly use this repo. Please star it if you like :)

**Instructions:**
1. Fork this repo to your own account
2. Go to: your-own-repo -> Settings -> Secrets and variables -> Actions
3. Go to Secrets. Secrets are encrypted and are used for sensitive data
4. Create two repository secrets named `OPENAI_API_KEY` and `OPENAI_BASE_URL`, and input corresponding values.
5. Go to Variables. Variables are shown as plain text and are used for non-sensitive data
6. Create the following repository variables:
   1. `CATEGORIES`: separate the categories with ",", such as "cs.GR, cs.CV"
   2. `LANGUAGE`: such as "Chinese" or "English"
   3. `MODEL_NAME`: such as "deepseek-chat"
   4. `EMAIL`: your email for push to github
   5. `NAME`: your name for push to github
7. Go to your-own-repo -> Actions -> arXiv-daily-ai-enhanced
8. You can manually click **Run workflow** to test if it works well (it may takes about one hour). 
By default, this action will automatically run every day
You can modify it in `.github/workflows/run.yml`
9. If you wish to modify the content in `README.md`, do not directly edit README.md. You should edit `template.md`.

# To-do list
- [ ]  Replace markdown with GitHub pages front-end.

# Content
[2025-09-23](data/2025-09-23.md)

[2025-09-22](data/2025-09-22.md)

[2025-09-21](data/2025-09-21.md)

[2025-09-20](data/2025-09-20.md)

[2025-09-19](data/2025-09-19.md)

[2025-09-18](data/2025-09-18.md)

[2025-09-17](data/2025-09-17.md)

[2025-09-16](data/2025-09-16.md)

[2025-09-15](data/2025-09-15.md)

[2025-09-14](data/2025-09-14.md)

[2025-09-13](data/2025-09-13.md)

[2025-09-12](data/2025-09-12.md)

[2025-09-11](data/2025-09-11.md)

[2025-09-10](data/2025-09-10.md)

[2025-09-09](data/2025-09-09.md)

[2025-09-08](data/2025-09-08.md)

[2025-09-07](data/2025-09-07.md)

[2025-09-06](data/2025-09-06.md)

[2025-09-05](data/2025-09-05.md)

[2025-09-04](data/2025-09-04.md)

[2025-09-03](data/2025-09-03.md)

[2025-09-02](data/2025-09-02.md)

[2025-09-01](data/2025-09-01.md)

[2025-08-31](data/2025-08-31.md)

[2025-08-30](data/2025-08-30.md)

[2025-08-29](data/2025-08-29.md)

[2025-08-28](data/2025-08-28.md)

[2025-08-27](data/2025-08-27.md)

[2025-08-26](data/2025-08-26.md)

[2025-08-25](data/2025-08-25.md)

[2025-08-24](data/2025-08-24.md)

[2025-08-23](data/2025-08-23.md)

[2025-08-22](data/2025-08-22.md)

[2025-08-21](data/2025-08-21.md)

[2025-08-20](data/2025-08-20.md)

[2025-08-19](data/2025-08-19.md)

[2025-08-18](data/2025-08-18.md)

[2025-08-17](data/2025-08-17.md)

[2025-08-16](data/2025-08-16.md)

[2025-08-15](data/2025-08-15.md)

[2025-08-14](data/2025-08-14.md)

[2025-08-13](data/2025-08-13.md)

[2025-08-12](data/2025-08-12.md)

[2025-08-11](data/2025-08-11.md)

[2025-08-10](data/2025-08-10.md)

[2025-08-09](data/2025-08-09.md)

[2025-08-08](data/2025-08-08.md)

[2025-08-07](data/2025-08-07.md)

[2025-08-06](data/2025-08-06.md)

[2025-08-05](data/2025-08-05.md)

[2025-08-04](data/2025-08-04.md)

[2025-08-03](data/2025-08-03.md)

[2025-08-02](data/2025-08-02.md)

[2025-08-01](data/2025-08-01.md)

[2025-07-31](data/2025-07-31.md)

[2025-07-30](data/2025-07-30.md)

[2025-07-29](data/2025-07-29.md)

[2025-07-28](data/2025-07-28.md)

[2025-07-27](data/2025-07-27.md)

[2025-07-26](data/2025-07-26.md)

[2025-07-25](data/2025-07-25.md)

[2025-07-24](data/2025-07-24.md)

[2025-07-23](data/2025-07-23.md)

[2025-07-22](data/2025-07-22.md)

[2025-07-21](data/2025-07-21.md)

[2025-07-20](data/2025-07-20.md)

[2025-07-19](data/2025-07-19.md)

[2025-07-18](data/2025-07-18.md)

[2025-07-17](data/2025-07-17.md)

[2025-07-16](data/2025-07-16.md)

[2025-07-15](data/2025-07-15.md)

[2025-07-14](data/2025-07-14.md)

[2025-07-13](data/2025-07-13.md)

[2025-07-12](data/2025-07-12.md)

[2025-07-11](data/2025-07-11.md)

[2025-07-10](data/2025-07-10.md)

[2025-07-09](data/2025-07-09.md)

[2025-07-08](data/2025-07-08.md)

[2025-07-07](data/2025-07-07.md)

[2025-07-06](data/2025-07-06.md)

[2025-07-05](data/2025-07-05.md)

[2025-07-04](data/2025-07-04.md)

[2025-07-03](data/2025-07-03.md)

[2025-07-01](data/2025-07-01.md)

[2025-06-30](data/2025-06-30.md)

[2025-06-29](data/2025-06-29.md)

[2025-06-28](data/2025-06-28.md)

[2025-06-27](data/2025-06-27.md)

[2025-06-26](data/2025-06-26.md)

[2025-06-25](data/2025-06-25.md)

[2025-06-24](data/2025-06-24.md)

[2025-06-23](data/2025-06-23.md)

[2025-06-22](data/2025-06-22.md)

[2025-06-21](data/2025-06-21.md)

[2025-06-20](data/2025-06-20.md)

[2025-06-19](data/2025-06-19.md)

[2025-06-18](data/2025-06-18.md)

[2025-06-17](data/2025-06-17.md)

[2025-06-16](data/2025-06-16.md)

[2025-06-15](data/2025-06-15.md)

[2025-06-14](data/2025-06-14.md)

[2025-06-13](data/2025-06-13.md)

[2025-06-12](data/2025-06-12.md)

[2025-06-11](data/2025-06-11.md)

[2025-06-10](data/2025-06-10.md)

[2025-06-09](data/2025-06-09.md)

# Related tools
- ICML, ICLR, NeurIPS list: https://dw-dengwei.github.io/OpenReview-paper-list/index.html

# Star history

[![Star History Chart](https://api.star-history.com/svg?repos=dw-dengwei/daily-arXiv-ai-enhanced&type=Date)](https://www.star-history.com/#dw-dengwei/daily-arXiv-ai-enhanced&Date)
