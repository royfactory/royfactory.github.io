---
layout: post

#event information
title:  "리눅스에서 Apache HTTP Server 설정하는 방법"
cover: "/img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg"
categories: linux
date: 2024-11-11
tags: linux apache http httpd config httpd.conf

toc: true

#event organiser details
organiser: "Royfactory"


---

# 리눅스에서 Apache HTTP Server 설정하는 방법

Apache HTTP Server(`httpd`)는 리눅스에서 널리 사용되는 웹 서버입니다. `httpd.conf` 설정 파일을 통해 다양한 서버 옵션을 조정할 수 있는데, 이번 글에서는 서버를 설정할 때 자주 사용하는 주요 항목들과 그 예시를 소개하겠습니다.

---

## 1. ServerRoot
서버의 루트 디렉토리를 지정하는 설정입니다. Apache는 이 데릭토리에서 로그 파일이나 설정 파일을 찾습니다.
```apache
ServerRoot "/etc/httpd"
```
기본적으로 `/etc/httpd` 경로를 많이 사용합니다.

---

## 2. Listen
서버가 요청을 대기할 포트와 IP 주소를 설정하는 항목입니다. 기본적으로 웹서버는 80 포트를 사용하지만, 이 설정ㅇ르 통해 다른 포트를 지정할 수 있습니다.
```apache
Listen 80
Listen 8080
```
이 예제에서는 80포트와 8080포트에서 요청을 대기하도록 설정했습니다.

---

## 3. DocumentRoot
`DocumentRoot`는 웹 서버의 기본 문서 경로를 지정하는 설정입니다. 이 디렉토리에 있는 파일들이 클라이언트에게 제공됩니다. 예를 들어, `index.html` 파일이 여기에 위치하게 됩니다.
```apache
DocumentRoot "/var/www/html"
```

---

## 4. ServerAdmin
서버 관리자 이메일을 지정하는 옵션입니다. 에러 페이지에 이 이메일을 표시할 수 있어, 방문자가 문제 발생 시 관리자에게 연락할 수 있게 됩니다.
```apache
ServerAdmin webmaster@example.com
```

---

## 5. ServerName
서버의 호스트 이름과 포트를 지정하는 설정입니다. 도메인 이름을 지정하여 클라이언트가 이를 통해 접근할 수 있도록 합니다.
```apache
ServerName www.example.com:80
```

---

## 6. Directory
특정 디렉토리에 대한 접근 권한과 설정을 정의합니다. `AllowOverride`, `Options`, `Require` 등 세부 지시문을 통해 디렉토리 접근을 제어할 수 있습니다.
```apache
<Directory "/var/www/html">
   Options Indexes FollowSymLinks
   AllowOverride None
   Require all granted
</Directory>
```
이 예제에서는 `/var/www/html` 디렉토리의 접근 권한을 설정했습니다.

---

## 7. Options
`Options`는 디렉토리 내에서 허용할 기능을 정의하는 항목입니다. 예를 들어, `Indexes`, `FollowSymLinks`, `ExecCGI` 등을 사용할 수 있습니다.
```apache
Options Indexes FollowSymLinks
여기서는 파일 인덱스 표시와 심볼릭 링크를 따르는 옵션을 활성화했습니다.
```

---

## 8. ErrorLog
서버 에러 로그 파일의 경로르 지정합니다. 서버 운영 중 발생하는 에러 기록을 통해 문제를 확인하고 디버깅할 수 있습니다.
```apache
ErrorLog "/var/log/httpd/error_log"
```

---

## 9. CustomLog
클라이언트 요청에 대한 접근 로그를 기록하는 파일을 지정합니다. 이를 통해 사이트 방문자 활동을 추적할 수 있습니다.
```apache
CustomLog "/var/log/httpd/access_log" combined
```

---

## 10. Alias
특정 URL을 다른 디렉토리로 매핑하는 설정입니다. 예를 들어, `/images` URL을 `/var/www/images` 디렉토리로 연결할 수 있습니다.
```apache
Alias /images "/var/www/images"
<Directory "/var/www/images">
   AllowOverride None
   Require all granted
</Directory>
```

---

## 11. VirtualHost
하나의 서버에서 여러 도메인을 호스팅할 수 있도록 해주는 설정입니다. 각 도메인에 대해 별도로 설정할 수 있어 다양한 사이트를 하나의 서버에서 운영할 수 있습니다.
```apache
<VirtualHost *:80>
   ServerAdmin webmaster@example1.com
   DocumentRoot "/var/www/example1"
   ServerName www.example1.com
   ErrorLog "/var/log/httpd/example1_error_log"
   CustomLog "/var/log/httpd/example1_access_log" combined
</VirtualHost>

<VirtualHost *:80>
   ServerAdmin webmaster@example2.com
   DocumentRoot "/var/www/example2"
   ServerName www.example2.com
   ErrorLog "/var/log/httpd/example2_error_log"
   CustomLog "/var/log/httpd/example2_access_log" combined
<VirtualHost>
```

---

## 12. LimitRequestBody
클라이언트가 서버로 전송할 수 있는 요청 본문 크기를 제한하는 설정입니다. 파일 업로드를 제한하거나, 서버 과부하를 방지할 수 있습니다.
```apache
LimitRequestBody 10485760  # 10MB
```

---

## 13. KeepAlive
`KeepAlive`는 클라이언트와 서버 간의 지속적인 연결 여부를 설정합니다. `On`으로 설정하면 클라이언트가 여러 요청을 한 번의 연결로 처리할 수 있어 성능이 향상됩니다.
```apache
KeepAlive On
```

---

Apache 설정을 제대로 이해하고 사용하면 웹 서버의 성능을 최적화하고 보안을 가오하할 수 있습니다. 위의 설정 항목들을 적절히 조합하여 본인 서버 환경에 맞게 설정해보시길 바랍니다.

---



