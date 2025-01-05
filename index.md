---
layout: default
title: Research Paper Repository
---

<style>
body {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
}

h1 {
  color: #2c3e50;
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 30px;
}

#category-select {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

#paper-list {
  list-style-type: none;
  padding: 0;
}

#paper-list li {
  background-color: #fff;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

#paper-list li:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

#paper-list a {
  color: #3498db;
  text-decoration: none;
  font-weight: bold;
}

#paper-list a:hover {
  color: #2980b9;
}

#paper-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  margin-top: 20px;
}
</style>

# Research Paper Repository

<select id="category-select">
  <option value="">Select a category</option>
</select>

<ul id="paper-list"></ul>

<div id="paper-content"></div>

<script>
const categorySelect = document.getElementById('category-select');
const paperList = document.getElementById('paper-list');
const paperContent = document.getElementById('paper-content');

// Function to fetch and populate categories
async function fetchCategories() {
  const response = await fetch('https://api.github.com/repos/hiroyokoi/researchpapers/contents/Research_papers');
  const data = await response.json();
  const categories = data.filter(item => item.type === 'dir').map(item => item.name);
  
  categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category;
    categorySelect.appendChild(option);
  });
}

// Function to fetch and display papers for a category
async function fetchPapers(categor
