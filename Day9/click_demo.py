import click

@click.command()
@click.option('--string', default ='World', help ='This is a greeting')
def hello(string):
	click.echo(f"Hello, {string}")

if __name__=="__main__":
  hello()	
