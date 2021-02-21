---
author: Author Name
title: Title of Slide
subtitle: Subtitle of Slide (optional)
acknowledgements: Acknowledgements (optional)
title-slide-attributes:
    data-background-image: logo.png
    data-background-size: auto 75px
    data-background-position: bottom 25px left 25px
    data-background-opacity: .3
---



### Slide title 1

Some highlighted code

```{data-line-numbers=1|2-3|4}
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```

### Slide with a pause

content before the pause

. . .

content after the pause

### Slide title 2

A list

* test
* test

### Slide title 3
:::::::::::::: {.columns}
::: {.column width="40%"}
contents...
:::
::: {.column .fragment width="60%"}
```{data-line-numbers=1|2}
def hello_world():
    print("Hello world!")
```
:::
::::::::::::::
