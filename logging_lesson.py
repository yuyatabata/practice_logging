import logging

formatter = '%(levelname)s : %(asctime)s : %(message)s'

logging.basicConfig(filename='logfile/logger.log',level=logging.INFO, format=formatter)

logging.info('%s %s', 'test', 'test')

# logging.info('error{}'.format('outputting error'))
# logging.info('warning %s %s' % ('was', 'outputted'))
# logging.info('info %s %s', 'test', 'test')

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

