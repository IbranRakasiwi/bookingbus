 5.49 KB
 
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="description" content="" />
    <meta name="author" content="" />
    <title>Home</title>
    <link href="{% static 'css/dist/css/styles.css' %}" rel="stylesheet" />
    <link href="{% static 'css/dist/js/dataTables.bootstrap4.min.css' %}" rel="stylesheet" crossorigin="anonymous" />
    <link rel="stylesheet" href="{% static 'css/assets/css/bootstrap.css' %}">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/js/all.min.js"
        crossorigin="anonymous"></script>
</head>

<body class="sb-nav-auto">
    <nav class="sb-topnav navbar navbar-expand navbar-dark bg-dark">
        <a class="navbar-brand" href="/">SIM-PKL</a>
        <button class="btn btn-link btn-sm order-1 order-lg-0" id="sidebarToggle" href="#"><i
                class="fas fa-bars"></i></button>
        <!-- Navbar Search
            <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-3 my-2 my-md-0">
                <div class="input-group">
                    <input class="form-control" type="text" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2" />
                    <div class="input-group-append">
                        <button class="btn btn-primary" type="button"><i class="fas fa-search"></i></button>
                    </div>
                </div>
            </form> -->
        <!-- Navbar-->
        <ul class="navbar-nav ml-auto ml-md-12">
            <li class="nav-item">
                <a class="nav-link disabled" href="#">{{user}}</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" id="userDropdown" href="#" role="button" data-toggle="dropdown"
                    aria-haspopup="true" aria-expanded="false"><i class="fas fa-user fa-fw"></i></a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
                    <a class="dropdown-item" href="#">Settings</a>
                    <a class="dropdown-item" href="#">Activity Log</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="/accounts/logout">Logout</a>
                </div>
            </li>
        </ul>
    </nav>
</body>
<div id="layoutSidenav">
    <div id="layoutSidenav_nav">
        <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
            <div class="sb-sidenav-menu">
                <div class="nav">
                    <div class="sb-sidenav-menu-heading">Interface</div>
                    <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseLayouts"
                        aria-expanded="false" aria-controls="collapseLayouts">
                        <div class="sb-nav-link-icon"><i class="fas fa-tachometer-alt"></i></div>
                        Dashboard
                        <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                    </a>
                    <div class="collapse" id="collapseLayouts" aria-labelledby="headingOne"
                        data-parent="#sidenavAccordion">
                        <nav class="sb-sidenav-menu-nested nav">
                            <a class="nav-link" href="/mahasiswa">Pendaftaran PKL</a>
                            <a class="nav-link" href="/catatan">Manajemen PKL</a>
                        </nav>
                    </div>
                    <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapsePages"
                        aria-expanded="false" aria-controls="collapsePages">
                        <div class="sb-nav-link-icon"><i class="fas fa-book-open"></i></div>
                        Manajement
                        <div class="sb-sidenav-collapse-arrow"><i class="fas fa-angle-down"></i></div>
                    </a>
                    <div class="collapse" id="collapsePages" aria-labelledby="headingTwo"
                        data-parent="#sidenavAccordion">
                        <nav class="sb-sidenav-menu-nested nav accordion" id="sidenavAccordionPages">
                            <a class="nav-link" href="/mitra">Mitra</a>
                        </nav>
                    </div>
        </nav>
    </div>


    <!-- Main content -->
    <div id="layoutSidenav_content">
        <main>
            {% block content %}
            {% include "messages.html" %}
            <!-- # isi konten -->
            {% endblock %}
            <main>
    </div>
    <script src="{% static 'css/dist/js/jquery-3.5.1.min.js' %}" crossorigin="anonymous"></script>
    <script src="{% static 'css/dist/js/bootstrap.bundle.min.js' %}" crossorigin="anonymous"></script>
    <script src="{% static 'css/dist/js/scripts.js' %}"></script>
    <script src="{% static 'css/dist/js/Chart.min.js' %}" crossorigin="anonymous"></script>
    <script src="{% static 'css/dist/assets/demo/chart-area-demo.js' %}"></script>
    <script src="{% static 'css/dist/assets/demo/chart-bar-demo.js' %}"></script>
    <script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js" crossorigin="anonymous"></script>
    <script src="{% static 'css/dist/js/dataTables.bootstrap4.min.js' %}" crossorigin="anonymous"></script>
    <script src="{% static 'css/dist/assets/demo/datatables-demo.js' %}"></script>
    </body>

</html>