# How to set up and modify this course website

## Install Hugo

Download the Hugo `.tar` file from [Hugo Releases](https://github.com/gohugoio/hugo/releases).

Set the environment path: link the Hugo binary file.

Verify the Hugo version:

```bash
hugo version
```

Now the repo is already a hugo site.

(Optional) If you want to initialize your own Hugo site, run:

```bash
hugo new site .
```

## Add the Geekdoc Theme

```bash
cd /path/to/repo
git submodule add https://github.com/thegeeklab/hugo-geekdoc.git themes/hugo-geekdoc
```

## Install Node.js (v20.19.0)

First, install `nvm` and set the environment variable:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Then, run the following commands to install Node.js:

```bash
nvm install 20
nvm use 20
nvm alias default 20
```

## Modify the gh-pages.yaml

The `gh-pages.yaml` file is located under `.github/workflows`.

- Update `hugo-version` to match your downloaded version.
- `publish_branch` is the branch that will be deployed other than `main`. You don't need to modify this if you are using `gh-pages` as your deploy branch.

## Configure the site

Modify the `config.yaml` file under the `config` directory:

- `baseURL` is your homepage domain.
- `title` is the homepage title.

The document of `hugo-geekdoc` is available at https://jlumbroso.github.io/hugo-geekdoc-github-example/usage/configuration/.
## Modify the site content

Content: Markdown files under the `content` directory.

Menu: Data files under `data/menu/*.yaml` files.

## Deploy the Geekdoc theme for the first time

```bash
cd themes/hugo-geekdoc
npm install
npm run build
```

Note: Every time you change the theme, you need to redeploy the Geekdoc theme. Otherwise, this is a one-time setup.

## Test site locally

Run the following command to start a local server:

```bash
hugo server --baseURL=http://localhost:1313/
```

Then open http://localhost:1313/ in your browser to view your site.

## Deploy the Site

Please first add the `public` directory to `.gitignore`.

I've already set up the GitHub Action to build and deploy the site automatically.

You can simply `git push` your changes to deploy the updated site.

If you want to set up your own homepage, you can refer to this guide: https://gohugo.io/host-and-deploy/host-on-github-pages/ to set up your own GitHub Action.

## Troubleshooting

If you encounter a "404 Not Found" error on your GitHub Pages site, go to your GitHub repository settings, select "GitHub Actions" and modify the `publish_branch` to "gh-pages".


