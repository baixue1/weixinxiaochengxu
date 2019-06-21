for (var i = 0;i< res.data.response.docs.length;i++)
         console.log( res.data.highlighting[res.data.response.docs[i].id])
for (var i = 0; i < res.data.response.docs.length; i++)
        {
          if (res.data.highlighting[res.data.response.docs[i].id] !== null)
           { console.log(res.data.response.docs[i].id)}
          }
      
      }
var s=[]
        for (var i = 0; i < res.data.response.docs.length; i++)
        {
          if (res.data.highlighting[res.data.response.docs[i].id] !== null)
          s[i] = { 'id': res.data.response.docs[i].id}
         
        }
        console.log(s)
 for (var i = 0; i < res.data.response.docs.length; i++)
        {
          for (var j = 0; j < s.length; j++)
          {
            if(res.data.response.docs[i].id !==s[j].id)
            {
              res.data.response.docs[i].SI_title = res.data.res.data.response.highlighting[j].SI_title
            }

          }
        }
    console.log(res.data.response.docs[2])
