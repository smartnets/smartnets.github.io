# SmartNets Website

Welcome to the SmartNets GitHub Pages website! This website is built using Jekyll, a static site generator, uses the [TeXt-theme](https://github.com/kitian616/jekyll-TeXt-theme) and is hosted on GitHub Pages. This README provides instructions on how to use and update the website.

## Getting Started

### Cloning the Repository

To get started, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/smartnets.github.io.git
```


## Installing Jekyll

Before running the website locally, you need to have Jekyll installed on your machine. Follow the instructions here to install Jekyll.

### Running the Website Locally

Once Jekyll is installed, navigate to the root directory of the cloned repository and run the following command:

```bash
bundle exec jekyll serve
```

This will build the website and serve it locally. You can then view the website by opening your web browser and navigating to `http://localhost:4000`.
## Updating the Website

### Overview of Structure

The structure of the code includes various folders and files:

- _members: Contains Markdown files for each member's bio.
- _posts: Stores Markdown files for blog posts.
- _research: Holds Markdown files for research topics.
- _data: Contains YAML and JSON files for configuration and data.
- _includes: Includes HTML snippets for reusable components.
- _layouts: Stores HTML layouts for different pages.
- _sass: Contains Sass files for styling.
- _site: Auto-generated folder containing the built website.
- research.md: The research page.
- publications.md: The publications page.
- news.md: The news page.
- members.md: The members page.
- smartnets.md: The website's homepage.
- semantic_scholar.py: The script for automatically fetching recent publications.

Other folders and files for configuration, assets, and additional functionalities.

### Updating User Bios

User bios are stored in the `_members` folder. To update a user's bio, navigate to the `_members` folder and edit the corresponding Markdown file. Each Markdown file represents a user's profile. Put the user's profile image at `/assets/images/`. The easier way for creating a new user is to copy-paste an existing one and to change the relevant details.

### Adding Posts

New posts can be added to the `_posts` folder. Create a new Markdown file in the `_posts` folder with the following filename format: YYYY-MM-DD-post-title.md. Then, add your post content to the Markdown file.

### Adding Research Topics

Research topics can be added to the `_research` folder. Create a new Markdown file in the `_research` folder with the content of the research topic.


## Committing and Pushing Changes

After making your changes, commit your changes using Git and push them to the repository:

```bash
git add .
git commit -m "Update website with new content"
git push origin main
```

Your changes will be reflected on the website soon after pushing to the repository.