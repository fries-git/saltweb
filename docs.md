# Saltweb Documentation

## Basic Understanding

Every line of content in your .sw file corresponds to a line in the "compiled" html file.

Each line is broken up into: [tag]{content} and tag case (upper/lower) is unimportant.

*Also note how even if you have any combination of {} or [] in the content, it still works.*

## List of Tags

header -> /h1

chapter -> /h2

section -> /h3

body -> /p

footer -> footer

link -> a

pagelink -> *Pagelink is a unique tag that takes you to the page at content. So: [pagelink]{docs} would take you to server/docs. Its the path to your file.

[github.com/fries-git/saltweb](https://github.com/fries-git/saltweb)