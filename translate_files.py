#!/usr/bin/env python3

import os
import sys
import click

from googleapiclient.discovery import build

TAB='\t'
HACK_TAB_REPLACEMENT='----'

@click.command()
@click.option('--source', required=True, help='Source language')
@click.option('--target', required=True, help='Target language')
@click.option('--apikey', envvar='GOOGLE_API_KEY', help='Google API key  [default read from GOOGLE_API_KEY]')
@click.argument('paths', nargs=-1)
def main(apikey, source, target, paths):
  service = build('translate', 'v2', developerKey=apikey)

  # Construct a large batch request.
  # Just ignore each file that cannot be read into a string.
  goodPaths = []
  texts = []
  for path in paths:
    try:
      with open(path, encoding='utf-8') as f:
        texts.append(f.read())
        goodPaths.append(path)
    except Exception as e:
      print(f'{path}:', e, file=sys.stderr)

  if len(texts) > 0:
    # Hack to preserve TAB.
    encodedTexts = [text.replace(TAB, HACK_TAB_REPLACEMENT) for text in texts]

    request = service.translations().list(
      format='text',
      source=source,
      target=target,
      q=encodedTexts
    )

    # {translations': [{translatedText': fleur'}, {translatedText': voiture'}]}
    response = request.execute()

    # Extract result for each text.
    for path, translation in zip(goodPaths, response['translations']):
      translatedText = translation['translatedText']
      decodedText = translatedText.replace(HACK_TAB_REPLACEMENT, TAB)
      translatedPath = f'{path}.output'
      try:
        with open(translatedPath, 'w', encoding='utf-8') as f:
          f.write(decodedText)
      except Exception as e:
        print(f'{translatedPath}:', e, file=sys.stderr)


if __name__ == '__main__':
    main()
