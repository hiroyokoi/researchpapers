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

let categories = [];
let papers = {};

// Function to fetch and populate categories
async function fetchCategories() {
  try {
    const response = await fetch('/data/categories.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    categories = await response.json();
    
    categories.forEach(category => {
      const option = document.createElement('option');
      option.value = category;
      option.textContent = category;
      categorySelect.appendChild(option);
    });
  } catch (error) {
    console.error("Failed to fetch categories:", error);
    categorySelect.innerHTML = '<option value="">Error loading categories</option>';
  }
}

// Function to fetch and display papers for a category
async function fetchPapers(category) {
  try {
    if (!papers[category]) {
      const response = await fetch(`/data/${category}.json`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      papers[category] = await response.json();
    }
    
    paperList.innerHTML = '';
    papers[category].forEach(paper => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = '#';
      a.textContent = paper.title;
      a.onclick = (e) => {
        e.preventDefault();
        fetchPaperContent(category, paper.title);
      };
      li.appendChild(a);
      paperList.appendChild(li);
    });
  } catch (error) {
    console.error(`Failed to fetch papers for ${category}:`, error);
    paperList.innerHTML = '<li>Error loading papers</li>';
  }
}

// Function to fetch and display paper content
async function fetchPaperContent(category, title) {
  try {
    const response = await fetch(`/Research_papers/${category}/${title}/${title}.md`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const content = await response.text();
    paperContent.innerHTML = marked.parse(content);
  } catch (error) {
    console.error(`Failed to fetch content for ${title}:`, error);
    paperContent.innerHTML = 'Error loading paper content';
  }
}

// Event listener for category selection
categorySelect.addEventListener('change', (e) => {
  if (e.target.value) {
    fetchPapers(e.target.value);
  } else {
    paperList.innerHTML = '';
    paperContent.innerHTML = '';
  }
});

// Initialize categories on page load
document.addEventListener('DOMContentLoaded', async () => {
  await fetchCategories();
});
</script>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>