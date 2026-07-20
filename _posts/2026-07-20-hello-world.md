---
title: "使用 Jekyll + Minimal Mistakes 搭建个人博客并部署到 GitHub Pages"
date: 2026-07-20
last_modified_at: 2026-07-20
categories:
  - 技术
  - 教程
tags:
  - Jekyll
  - GitHub Pages
  - 博客
  - Minimal Mistakes
  - 教程
toc: true
toc_label: "目录"
toc_icon: "list"
---

## 前言

作为一个开发者，拥有一个属于自己的技术博客是件很酷的事。你可以在上面记录学习笔记、分享项目经验、沉淀知识体系。本文将带你从零开始，使用 **Jekyll** 静态站点生成器和 **Minimal Mistakes** 主题，搭建一个功能完备的个人博客，并免费部署到 GitHub Pages。

## 为什么选 Jekyll + Minimal Mistakes？

### Jekyll 的优势

- **原生 GitHub Pages 支持**：推送即部署，无需额外配置 CI/CD
- **无需数据库**：纯静态文件，加载速度快，安全性高
- **Markdown 写作**：使用熟悉的 Markdown 语法写文章，Git 管理版本
- **模板系统**：Liquid 模板引擎，灵活可定制

### Minimal Mistakes 的特点

- **功能开箱即用**：搜索、标签、分类、评论、SEO、RSS 全部内置
- **响应式设计**：完美适配桌面和移动端
- **多皮肤支持**：内置亮色/暗色多种主题皮肤
- **社区活跃**：GitHub 上 13.5k+ Stars，文档完善

## 环境准备

首先确保你的开发环境已安装以下工具：

```bash
# 检查 Ruby 环境
ruby --version

# 检查 Bundler
gem --version
```

如果没有安装 Ruby，可以从 [ruby-lang.org](https://ruby-lang.org) 下载安装。

> **小贴士**：在 Windows 上安装 Ruby 建议使用 [RubyInstaller](https://rubyinstaller.org/)，记得勾选 "Add Ruby executables to your PATH"。

## 创建项目

### 1. 初始化 Jekyll 站点

```bash
# 创建新站点
jekyll new my-blog
cd my-blog

# 启动本地开发服务器
bundle exec jekyll serve
```

访问 `http://localhost:4000` 即可看到默认站点。

### 2. 更换为 Minimal Mistakes 主题

编辑 `Gemfile`，添加：

```ruby
gem "minimal-mistakes-jekyll"
```

编辑 `_config.yml`：

```yaml
remote_theme: "mmistakes/minimal-mistakes"
minimal_mistakes_skin: "dark"

title: "我的博客"
locale: "zh-CN"
url: "https://你的用户名.github.io"
```

然后执行：

```bash
bundle install
```

### 3. 目录结构说明

```
my-blog/
├── _config.yml          # 站点配置文件
├── _posts/              # 博客文章 (Markdown)
├── _data/               # 数据文件 (导航、翻译等)
├── _pages/              # 自定义页面
├── assets/              # 静态资源 (CSS/JS/图片)
├── _includes/           # 可复用的模板片段
├── _layouts/            # 页面布局模板
└── index.html           # 首页
```

## 核心功能配置

### 导航菜单

`_data/navigation.yml`：

```yaml
main:
  - title: "首页"
    url: /
  - title: "文章"
    url: /posts/
  - title: "标签"
    url: /tags/
  - title: "关于"
    url: /about/
```

### 搜索功能

Minimal Mistakes 内置了 Lunr.js 客户端搜索：

```yaml
search: true
search_provider: lunr
```

### 标签和分类

```yaml
jekyll-archives:
  enabled:
    - tags
    - categories
  layouts:
    tag: archive-taxonomy
    category: archive-taxonomy
  permalinks:
    tag: /tags/:name/
    category: /categories/:name/
```

### 评论系统

集成 giscus（基于 GitHub Discussions）：

```yaml
comments:
  provider: giscus
giscus:
  repo: "用户名/仓库名"
  repo_id: "你的 repo_id"
  category: "General"
  category_id: "你的 category_id"
```

### 文章 Front Matter

每篇文章的开头需要包含 YAML 头部信息：

```yaml
---
title: "文章标题"
date: 2026-07-20
categories:
  - 技术
tags:
  - Jekyll
  - Web
toc: true
---
```

## 部署到 GitHub Pages

### 方法一：自动部署（推荐）

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy Jekyll site to Pages

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: "3.3"
          bundler-cache: true
      - uses: actions/jekyll-build-pages@v1
      - uses: actions/upload-pages-artifact@v3
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/deploy-pages@v4
```

### 方法二：自动检测

如果使用 `username.github.io` 仓库，GitHub Pages 会自动检测 Jekyll 项目并构建。只需推送 `main` 分支即可。

### 推送并上线

```bash
git init
git add .
git commit -m "Initial blog"
git remote add origin https://github.com/用户名/用户名.github.io.git
git branch -M main
git push -u origin main
```

等待 1-2 分钟，访问 `https://用户名.github.io` 即可看到你的博客。

## 进阶功能

### 添加自定义 CSS

在 `_includes/head/custom.html` 中引入：

```html
<link rel="stylesheet" href="/assets/css/custom.css">
```

### 添加音乐播放器

使用 APlayer + MetingJS 集成网易云音乐：

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/aplayer/1.10.1/APlayer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/meting@2.0.1/dist/Meting.min.js"></script>

<meting-js
  server="netease"
  type="playlist"
  id="你的歌单ID"
  fixed="true"
  mini="true"
  theme="#FF8C9E">
</meting-js>
```

### 亮色/暗色模式切换

通过 JavaScript + CSS 变量实现：

```javascript
function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
}
```

配合 CSS 中的 `[data-theme="dark"]` 选择器覆盖样式，实现无缝切换。

## 总结

通过 Jekyll + Minimal Mistakes + GitHub Pages 这个组合，我们仅用几个简单的步骤就搭建了一个功能完整的个人博客。这套方案的优势在于：

- ✅ **零成本**：域名托管全免费
- ✅ **易维护**：Markdown 写作，Git 管理
- ✅ **功能全**：搜索、标签、评论、RSS 一应俱全
- ✅ **可扩展**：Liquid 模板系统方便自定义

希望这篇教程对你有帮助！如果你有任何问题，欢迎在评论区留言交流。
