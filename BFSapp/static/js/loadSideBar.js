const loadSidebar = function () {
  const sideBarDiv = `<div class="sidebar" data-background-color="dark">
        <div class="sidebar-logo">
          <!-- Logo Header -->
          <div class="logo-header" data-background-color="dark">
                                    <img
                                      src="../static/img/logogood.png"
                                      alt="logo"
                                      class="navbar-brand" height="35
                                    />
            <!-- <a href="index.html" class="logo">
            </a> 
                       <button class="topbar-toggler more">
              <i class="gg-more-vertical-alt"></i>
            </button>
          </div>
         
        </div>
        <div class="sidebar-wrapper scrollbar scrollbar-inner">
          <div class="sidebar-content">
            <ul class="nav nav-secondary">
              <li class="nav-item active">
                <a
                  href="/index"
                  aria-expanded="false"
                >
                  <i class="fas fa-home"></i>
                  <p>Dashboard</p>
                </a>
              </li>
              <li class="nav-section">
                <span class="sidebar-mini-icon">
                  <i class="fa fa-ellipsis-h"></i>
                </span>
                <h4 class="text-section">Components</h4>
              </li>
              <li class="nav-item">
                <a data-bs-toggle="collapse" href="#forms">
                  <i class="fas fa-pen-square"></i>
                  <p>Insert Data</p>
                  <span class="caret"></span>
                </a>
                <div class="collapse" id="forms">
                  <ul class="nav nav-collapse">
                    <li class="active">
                      <a href="/forms/eggsMonitorForm"> 
                        <span class="sub-item">Eggs Monitoring</span>
                      </a>
                    </li>
                    <li>
                      <a href="/forms/rearingMonitorForm"> 
                        <span class="sub-item">Rearing Monitoring</span>
                      </a>
                    </li>
                    <li>
                      <a href="/forms/breedingMonitorForm"> 
                        <span class="sub-item">Breeding Monitoring</span>
                      </a>
                    </li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a data-bs-toggle="collapse" href="#tables">
                  <i class="fas fa-table"></i>
                  <p>Databases</p>
                  <span class="caret"></span>
                </a>
                <div class="collapse" id="tables">
                  <ul class="nav nav-collapse">
                    <li>
                      <a href="/tables/eggMonitorTable">
                        <span class="sub-item">Eggs Monitoring Table</span>
                      </a>
                    </li>
                    <li>
                      <a href="/tables/rearingMonitorTable">
                        <span class="sub-item">Rearing Monitoring Table</span>
                      </a>
                    </li>
                    <li>
                      <a href="/tables/breedingMonitorTable">
                        <span class="sub-item">Breeding Monitoring Table</span>
                      </a>
                    </li>
                  </ul>
                </div>
              </li>
              <li class="nav-item">
                <a href="/forms/predictionForm">
                  <i class="fas fa-desktop"></i>
                  <p>Predication</p>
                                 </a>
              </li>
            </ul>
          </div>
        </div>
      </div>`;
  const body = document.querySelector(".page-inner");
  body.insertAdjacentHTML("beforebegin", sideBarDiv);
};

loadSidebar();
