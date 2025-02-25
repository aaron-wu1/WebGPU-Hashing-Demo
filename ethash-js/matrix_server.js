const http = require('http')
const fs = require('fs')
const path = require('path')
const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
  if (req.url === '/' || req.url === '/webpage.html') {
    const filePath = path.join(__dirname, './matrix/', 'webpage.html')
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.statusCode = 500
        res.setHeader('Content-Type', 'text/plain')
        res.end('Internal Server Error')
      } else {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/html')
        res.end(data)
      }
    })
  } else if (req.url.endsWith('.js')) {
    const filePath = path.join(__dirname, './matrix/', req.url)
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.statusCode = 500
        res.setHeader('Content-Type', 'text/plain')
        res.end('Internal Server Error')
      } else {
        res.statusCode = 200
        res.setHeader('Content-Type', 'application/javascript')
        res.end(data)
      }
    })
  } else {
    res.statusCode = 404
    res.setHeader('Content-Type', 'text/plain')
    res.end('Not Found')
  }
})

server.listen(port, hostname, () => {
  console.log(`Server running at
   http://${hostname}:${port}/`)
})
