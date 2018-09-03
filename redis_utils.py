import redis
import random, time

class RedisHelper(object):
	def __init__(self):
		# self.__conn = redis.Redis(host='192.168.21.61',port=6379, password='123456Hb')#连接Redis
		self.__conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

	def publish(self, channel, msg):
		'''
		channel: 指定消息发送的频道
		msg: 消息内容
		'''
		self.__conn.publish(channel, msg)
		return True

	def subscribe(self, channel):
		'''
		channel: 指定接收消息的频道
		'''
		pub = self.__conn.pubsub()
		pub.subscribe(channel)
		pub.parse_response()
		return pub


if __name__ == '__main__':
	obj = RedisHelper()

	while True:
		time.sleep(1)
		print('publish')
		obj.publish('test1', '你哈')