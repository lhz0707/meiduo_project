# 日志记录器
import logging

# 创建日志记录器
logger=logging.getLogger('django')
# 输入日志
logger.debug("测试logging debug")
logger.info('测试loggin info')
logger.error('测试logginng error')