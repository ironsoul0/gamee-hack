from mitmproxy import ctx
from hashlib import md5
import json

def getChecksum(score, playTime, gameStateData, gameURL):
  string = "{}:{}:{}:{}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen"
  formatted = string.format(score, playTime, gameURL, gameStateData)
  return md5(formatted.encode('utf-8')).hexdigest()

def request(flow):
  request_url = flow.request.pretty_url
  if 'gamee' in request_url and len(flow.request.text) > 0:
    content = json.loads(flow.request.content)
    try:
      gameplayData = content['params']['gameplayData']

      checksum = gameplayData['checksum'] # proxy changes this value instantly
      playTime = gameplayData['playTime']
      gameStateData = gameplayData['gameStateData']
      url = gameplayData['gameUrl']

      desired_score = 1000
      content['params']['gameplayData']['score'] = desired_score

      score = desired_score
      
      ctx.log.info('Game state data is {}'.format(gameStateData))
      ctx.log.info('Score is {}'.format(score))
      ctx.log.info('Playtime is {}'.format(playTime))
      ctx.log.info('URL is {}'.format(url))
      ctx.log.info('Checksum is {}'.format(checksum))
      
      if score is None:
        score = ''
      if playTime is None:
        playTime = ''
      if gameStateData is None:
        gameStateData = ''
      if url is None:
        url = ''
      
      cur_checksum = getChecksum(score, playTime, gameStateData, url)
      content['params']['gameplayData']['checksum'] = cur_checksum
      
      flow.request.text = json.dumps(content)
      ctx.log.info('Body is {}'.format(flow.request.content))
    except:
      print('Exception..')