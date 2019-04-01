#!/usr/bin/python3


def tag(tag, *args, **kwargs):
    attrs = ''.join(f' {k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    html = f'<{tag}{attrs}>{inner}</{tag}>'
    return html.replace('css', 'class')


if __name__ == '__main__':
    html = tag('p',
               tag('span', 'Curso de Python 3, por '),
               tag('strong', 'Juracy Filho', id='jf'),
               tag('span', ' e '),
               tag('strong', 'Leonardo Leitão', id='ll'),
               tag('span', '.'),
               tag('strong', tag('span', '!!!')),
               css='alert')
    print(html)
