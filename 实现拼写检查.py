wx.request({
        //url: 'http://106.14.117.61:8983/solr/techproducts/select?indent=on&q=iPod&rows=15&wt=json',
        url: 'http://47.103.23.129:8983/solr/starinfo2/suggest?q=' + options.searchValue + '&rows=50',
        data: {},
        header: {
          'content-type': 'application/json' // 默认值
        },
        success: function (res) {
          //将获取到的json数据，存在名字叫list的这个数组中
          //that.setData({
          //list: res.data,
          //res代表success函数的事件对，data是固定的，list是数组

          console.log(res.data);
          // 赋值
          that.setData({
           list1: res.data.spellcheck.suggestions[1].suggestion,//可能需要根据json格式改路径
           loading: false,// 关闭等待框
          })
         console.log(res.data.spellcheck.suggestions[1].suggestion)
        }
      })
      
      
      
      
      
      
      <view class="suggest">您要输入的是否为：{{list1[0]}} {{list1[1]}} {{list1[2]}}</view>
