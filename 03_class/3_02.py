import tv

my4kTv = tv.Tv4K('65', 'sliver', '4k')
my4kTv.setSmartTv('on')
my4kTv.turnOn()
my4kTv.printTvInfo()
my4kTv.turnOff()

my8kTv = tv.Tv8K('75', 'black', '8k')
my8kTv.setSmartTv('on')
my8kTv.serAiTv('on')
my8kTv.turnOn()
my8kTv.printTvInfo()
my8kTv.turnOff()