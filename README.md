# Home Page of Helio Perroni Filho - Sources

Sources for my [personal website](http://xperroni.me).

## Updating

To build the site for local access and inspect changes, run:

    $ make html && make serve

Then access [the local runinng instance](http://localhost:8000) to check results.

Once satisfied with changes, generate the output with:

    $ make publish

In order to push changes, first push the `output` submodule, then the base repository:

    cd output
    git add -A .
    git commit -s -m <message>
    git push
    cd ..
    git add -A .
    git commit -s -m <message>
    git push

## References

* [Make a Github Pages blog with Pelican](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)
