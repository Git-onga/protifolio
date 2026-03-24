import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace skills
skills_carousel_html = """        <div class="skills-carousel reveal">
          <div class="carousel-track">
            <!-- Web Development -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="16 18 22 12 16 6"></polyline>
                  <polyline points="8 6 2 12 8 18"></polyline>
                </svg>
              </div>
              <h3>Web Development</h3>
              <p>HTML, CSS, and JavaScript — building responsive websites.</p>
            </div>

            <!-- 3D Animation -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12.89 1.45l8 4A2 2 0 0 1 22 7.24v9.53a2 2 0 0 1-1.11 1.79l-8 4a2 2 0 0 1-1.79 0l-8-4a2 2 0 0 1-1.1-1.8V7.24a2 2 0 0 1 1.11-1.79l8-4a2 2 0 0 1 1.78 0z"></path>
                  <polyline points="2.32 6.16 12 11 21.68 6.16"></polyline>
                  <line x1="12" y1="22.76" x2="12" y2="11"></line>
                </svg>
              </div>
              <h3>3D Animation</h3>
              <p>Modeling, texturing, rigging, and animation using Blender.</p>
            </div>

            <!-- Database Management -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                  <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                  <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
                </svg>
              </div>
              <h3>Database Management</h3>
              <p>Foundational skills in data storage, retrieval, and database design.</p>
            </div>

            <!-- Programming -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                  <line x1="8" y1="21" x2="16" y2="21"></line>
                  <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
              </div>
              <h3>Programming</h3>
              <p>Python, Java, Flutter, and other languages for diverse applications.</p>
            </div>

            <!-- Mobile App Developer -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect>
                  <line x1="12" y1="18" x2="12.01" y2="18"></line>
                </svg>
              </div>
              <h3>Mobile App Developer</h3>
              <p>Building cross-platform mobile apps using Dart and Flutter.</p>
            </div>

            <!-- Design -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 19l7-7 3 3-7 7-3-3z"></path>
                  <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path>
                  <path d="M2 2l7.586 7.586"></path>
                  <circle cx="11" cy="11" r="2"></circle>
                </svg>
              </div>
              <h3>Design</h3>
              <p>User interfaces and workflows with Figma and Canva.</p>
            </div>

            <!-- Machine Learning -->
            <div class="skill-card">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2a4 4 0 0 1 4 4c0 1.95-1.4 3.57-3.25 3.92a1 1 0 0 0-.75.97V13"></path>
                  <path d="M12 2a4 4 0 0 0-4 4c0 1.95 1.4 3.57 3.25 3.92a1 1 0 0 1 .75.97V13"></path>
                  <line x1="12" y1="13" x2="12" y2="17"></line>
                  <circle cx="12" cy="20" r="3"></circle>
                  <line x1="4" y1="20" x2="9" y2="20"></line>
                  <line x1="15" y1="20" x2="20" y2="20"></line>
                </svg>
              </div>
              <h3>Machine Learning</h3>
              <p>Beginning exploration in ML, data analysis, and visualization.</p>
            </div>

            <!-- DUPLICATED SKILLS FOR INFINITE SCROLL -->
            <!-- Web Development -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="16 18 22 12 16 6"></polyline>
                  <polyline points="8 6 2 12 8 18"></polyline>
                </svg>
              </div>
              <h3>Web Development</h3>
              <p>HTML, CSS, and JavaScript — building responsive websites.</p>
            </div>

            <!-- 3D Animation -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12.89 1.45l8 4A2 2 0 0 1 22 7.24v9.53a2 2 0 0 1-1.11 1.79l-8 4a2 2 0 0 1-1.79 0l-8-4a2 2 0 0 1-1.1-1.8V7.24a2 2 0 0 1 1.11-1.79l8-4a2 2 0 0 1 1.78 0z"></path>
                  <polyline points="2.32 6.16 12 11 21.68 6.16"></polyline>
                  <line x1="12" y1="22.76" x2="12" y2="11"></line>
                </svg>
              </div>
              <h3>3D Animation</h3>
              <p>Modeling, texturing, rigging, and animation using Blender.</p>
            </div>

            <!-- Database Management -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                  <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                  <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
                </svg>
              </div>
              <h3>Database Management</h3>
              <p>Foundational skills in data storage, retrieval, and database design.</p>
            </div>

            <!-- Programming -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                  <line x1="8" y1="21" x2="16" y2="21"></line>
                  <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
              </div>
              <h3>Programming</h3>
              <p>Python, Java, Flutter, and other languages for diverse applications.</p>
            </div>

            <!-- Mobile App Developer -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect>
                  <line x1="12" y1="18" x2="12.01" y2="18"></line>
                </svg>
              </div>
              <h3>Mobile App Developer</h3>
              <p>Building cross-platform mobile apps using Dart and Flutter.</p>
            </div>

            <!-- Design -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 19l7-7 3 3-7 7-3-3z"></path>
                  <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path>
                  <path d="M2 2l7.586 7.586"></path>
                  <circle cx="11" cy="11" r="2"></circle>
                </svg>
              </div>
              <h3>Design</h3>
              <p>User interfaces and workflows with Figma and Canva.</p>
            </div>

            <!-- Machine Learning -->
            <div class="skill-card" aria-hidden="true">
              <div class="skill-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2a4 4 0 0 1 4 4c0 1.95-1.4 3.57-3.25 3.92a1 1 0 0 0-.75.97V13"></path>
                  <path d="M12 2a4 4 0 0 0-4 4c0 1.95 1.4 3.57 3.25 3.92a1 1 0 0 1 .75.97V13"></path>
                  <line x1="12" y1="13" x2="12" y2="17"></line>
                  <circle cx="12" cy="20" r="3"></circle>
                  <line x1="4" y1="20" x2="9" y2="20"></line>
                  <line x1="15" y1="20" x2="20" y2="20"></line>
                </svg>
              </div>
              <h3>Machine Learning</h3>
              <p>Beginning exploration in ML, data analysis, and visualization.</p>
            </div>
          </div>"""

# Replace the block from <div class="skills-grid"> up to the end of the section
content = re.sub(r'<div class="skills-grid">.*?</div>\s*</div>\s*</section>', skills_carousel_html + '\n        </div>\n      </div>\n    </section>', content, flags=re.DOTALL)

new_projects_html = """          <!-- Project: Terafy -->
          <div class="project-card reveal">
            <div class="project-img">
              <img src="pics/terafy.png" alt="Terafy eco-friendly app interface">
            </div>
            <div class="project-body">
              <span class="project-date">August 2025</span>
              <h3>Terafy</h3>
              <p>An eco-friendly app that engages users in environmental activities for reward points.</p>
              <div class="tech-icons">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg" alt="Flutter" title="Flutter">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dart/dart-original.svg" alt="Dart" title="Dart">
              </div>
              <a href="#" class="project-link">View Project →</a>
            </div>
          </div>

          <!-- Project: Wander -->
          <div class="project-card reveal">
            <div class="project-img">
              <img src="pics/wander.png" alt="Wander international travel website">
            </div>
            <div class="project-body">
              <span class="project-date">September 2025</span>
              <h3>Wander</h3>
              <p>Website for international travel to book flights, accommodation, and transport.</p>
              <div class="tech-icons">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" title="HTML5">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" title="CSS3">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" title="JavaScript">
              </div>
              <a href="#" class="project-link">View Project →</a>
            </div>
          </div>

          <!-- Project 1: Food Delivery App -->"""
content = content.replace('<!-- Project 1: Food Delivery App -->', new_projects_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html')
