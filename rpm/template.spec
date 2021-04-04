%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-tf2-web-republisher
Version:        0.3.2
Release:        3%{?dist}%{?release_suffix}
Summary:        ROS tf2_web_republisher package

License:        BSD
URL:            http://ros.org/wiki/tf2_web_republisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2-ros
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Republishing of Selected TFs

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sun Apr 04 2021 Russell Toris <rctoris@wpi.edu> - 0.3.2-3
- Autogenerated by Bloom

* Sun Apr 04 2021 Russell Toris <rctoris@wpi.edu> - 0.3.2-2
- Autogenerated by Bloom

* Sun Apr 04 2021 Russell Toris <rctoris@wpi.edu> - 0.3.2-1
- Autogenerated by Bloom

