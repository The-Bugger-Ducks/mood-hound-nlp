import calculate_time

def init(topic):
  print('\n')
  print('=============================================================================')
  print(topic)
  calculate_time.init()

def finish_default():
  calculate_time.finish()
  print('-----------------------------------------------------------------------------')
  print('✅ Concluído com sucesso \n🕛:', calculate_time.get())
  print('=============================================================================')

def finish_variation():
  calculate_time.finish()
  print('-----------------------------------------------------------------------------')
  print('✅ Concluído com sucesso \n🕛:', calculate_time.get())
