var https = require('https');
var fs = require('fs');
var path = require('path');
var cheerio = require('cheerio');

// 爬虫的 URL 信息
var opt = {
    hostname: 'movie.douban.com',
    path: '/cinema/nowplaying/guangzhou/',
    port: 443
};

// 创建 http get 请求
https.get(opt, function(res) {
    var html = ''; // 保存抓取到的 HTML 源码
    var movies = [];  // 保存电影信息

    res.setEncoding('utf-8');

    // 抓取页面内容
    res.on('data', function(chunk) {
        html += chunk;
    });

    res.on('end', function() {
        var $ = cheerio.load(html);

        // 保存电影信息
        $('#nowplaying .list-item').each(function() {
            // 获取图片链接
            var movie = {
                title: $('.stitle a', this).attr('title'),
                star: $('.srating .subject-rate', this).html(),
                imgUrl: $('.poster a img', this).attr('src')
            };

            movies.push(movie);
        });

        // 保存抓取到的电影数据
        saveData('src/assets/data/data.json', movies);
    });
}).on('error', function(err) {
    console.log(err);
});

function saveData(path, movies) {
    // 调用 fs.writeFile 方法保存数据到本地
    fs.writeFile(path, JSON.stringify(movies, null, 3), function(err) {
        if (err) {
            return console.log(err);
        }
        console.log('Data saved');
    });
}
