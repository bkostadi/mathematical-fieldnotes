# Mathematical Field Notes

A Quarto teaching website for MAT 2580 and MAT 1372 at City Tech. The four editable pages and their rendered versions are included. The shear explorer runs in the browser. The probability lesson includes a base R experiment for students to run.

## Preview

Unzip the project and open `docs/index.html` in your browser. The pages, fonts, figures, and slider work locally.

To edit with live preview, open `MathematicalFieldNotes.Rproj` in RStudio, open the **Terminal** tab, and run the following command from the project folder.

```sh
quarto preview
```

This project was rendered with Quarto 1.9.38. The four pages render with the Quarto CLI alone. [Install Quarto](https://quarto.org/docs/get-started/).

## Publish the included website with GitHub Desktop

1. Sign in to GitHub and create a new repository, for example `mathematical-fieldnotes`. For GitHub Free, choose **Public**. Select **Add README** when creating the repository so the `main` branch exists.
2. In GitHub Desktop, choose **File → Clone Repository**, select the new repository, then **Clone**. Open the cloned folder in Finder or File Explorer.
3. Copy the **contents** of the unzipped project into the cloned folder. You should see `_quarto.yml` and `docs/` side by side at the repository root. Include the dotfiles. On a Mac, **Command + Shift + .** shows them in Finder.
4. In GitHub Desktop, enter a commit summary such as **Add Quarto teaching site**, choose **Commit to main**, then **Push origin**.
5. On the repository’s GitHub page, open **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**. Select **main**, select **/docs**, then choose **Save**.
6. Once deployment finishes, click **Visit site** on that same settings page.

A project named `mathematical-fieldnotes` has the default address `https://YOUR-USERNAME.github.io/mathematical-fieldnotes/`. For an account homepage at `https://YOUR-USERNAME.github.io/`, use the repository named `YOUR-USERNAME.github.io`. If you already have an account homepage, a separate project repository gives these notes their own address.

The first publication uses the included `docs/` folder. Signing in to GitHub yourself is sufficient. If you would like Codex to work in the repository and prepare pull requests, connect GitHub to Codex and select this repository in the GitHub App installation.

[Quarto’s GitHub Pages guide](https://quarto.org/docs/publishing/github-pages.html#render-to-docs) · [GitHub Pages settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [OpenAI’s Codex Cloud guide](https://learn.chatgpt.com/docs/cloud)

## Edit the website

| What to change | Where to edit |
| --- | --- |
| Homepage introduction and course links | `index.qmd` |
| Matrix lesson | `linear-algebra.qmd` |
| Dice lesson and R code | `probability.qmd` |
| Instructor introduction | `about.qmd` |
| Site title, navbar, and footer | `_quarto.yml` |
| Colors and typography | `assets/fieldnotes.css` |
| Shear figure and its controls | `_includes/shear.qmd` and `assets/shear.js` |

After editing a source file, run the following command in the RStudio terminal.

```sh
quarto render
```

Commit and push both the source changes and the updated `docs/` folder. GitHub Pages serves the rendered files from that folder.

To add a lesson, copy a lesson `.qmd`, change its page title and content, then link to the new `.qmd` from the relevant course page. Quarto rewrites that link to the corresponding HTML output.

## Artwork

The figures are original plots. Their PNG files are ready to use. To regenerate them after changing their geometry or colors, run `python3 tools/draw_figures.py` with Matplotlib and NumPy installed, then render the website. The bundled Instrument Serif and DM Sans fonts include their licenses in `assets/fonts/`.
