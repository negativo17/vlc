#global commit0 196cb1b2296ab46e9e9558108ec91b645de7370f
#global date 20201104
#global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag %{version}

Summary:    The cross-platform open-source multimedia framework, player and server
Name:       vlc
Version:    3.0.21
Release:    2%{!?tag:.%{date}git%{shortcommit0}}%{?dist}
Epoch:      2
License:    GPLv2+
URL:        http://www.videolan.org

%if 0%{?tag:1}
Source0:    https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
%else
Source0:    https://code.videolan.org/videolan/%{name}/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2#/%{name}-%{shortcommit0}.tar.bz2
%endif

Patch0:     %{name}-fdk-aac-v2.patch
Patch1:     %{name}-dvdread.patch
Patch2:     %{name}-crypto-policies.patch
Patch3:     https://src.fedoraproject.org/rpms/vlc/raw/rawhide/f/oneVPL.patch
Patch4:     https://src.fedoraproject.org/rpms/vlc/raw/rawhide/f/vaapi-without-ffmepg4.patch

BuildRequires:  aalib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  compat-lua
BuildRequires:  daala-devel
#BuildRequires:  decklink-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  game-music-emu-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  kf5-kdelibs4support-libs
BuildRequires:  liba52-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdvbpsi-devel
BuildRequires:  libebml-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmad-devel
BuildRequires:  libmatroska-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libtar-devel
BuildRequires:  libtool
BuildRequires:  lirc-devel
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:  yasm

BuildRequires:  pkgconfig(alsa) >= 1.0.24
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(aribb25) >= 0.2.6
BuildRequires:  pkgconfig(avahi-client) >= 0.6
BuildRequires:  pkgconfig(caca) >= 0.99.beta14
BuildRequires:  pkgconfig(cairo) >= 1.13.1
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dbus-1) >= 1.6.0
BuildRequires:  pkgconfig(dvdnav) > 4.9.0
BuildRequires:  pkgconfig(dvdread) > 4.9.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth) >= 1.1.2
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gnutls) >= 3.2.0
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack) >= 1.9.7
BuildRequires:  pkgconfig(libarchive) >= 3.1.0
BuildRequires:  pkgconfig(libass) >= 0.9.8
BuildRequires:  pkgconfig(libavc1394) >= 0.5.3
BuildRequires:	pkgconfig(libavcodec) >= 57.37.100
BuildRequires:	pkgconfig(libavformat) >= 53.21.0
BuildRequires:	pkgconfig(libavutil) >= 52.0.0
BuildRequires:  pkgconfig(libbluray) >= 0.6.2
BuildRequires:  pkgconfig(libcddb) >= 0.9.5
BuildRequires:  pkgconfig(libchromaprint) >= 0.6.0
BuildRequires:  pkgconfig(libdca) >= 0.0.5
BuildRequires:  pkgconfig(libdc1394-2) >= 2.1.0
BuildRequires:  pkgconfig(libidn)
#BuildRequires:  pkgconfig(libgoom2)
BuildRequires:  pkgconfig(libmodplug) > 0.8.9
BuildRequires:  pkgconfig(libmpeg2) > 0.3.2
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp) >= 1.0.0
BuildRequires:  pkgconfig(libnfs) >= 1.10.0
BuildRequires:  pkgconfig(libnotify)
#BuildRequires:  pkgconfig(libplacebo) >= 0.2.1
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.1
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.9.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
#BuildRequires:  pkgconfig(libsidplay2)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 142
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libvncclient) >= 0.9.9
#BuildRequires:  pkgconfig(libvsxu)
BuildRequires:  pkgconfig(live555)
BuildRequires:  pkgconfig(lua-5.1)
BuildRequires:  pkgconfig(microdns) >= 0.1.2
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(opus) >= 1.0.3
BuildRequires:  pkgconfig(protobuf-lite) >= 2.5.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5.0
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:  pkgconfig(sdl) >= 1.2.10
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(SDL_image) >= 1.2.10
#BuildRequires:  pkgconfig(shine) >= 3.0.0
BuildRequires:  pkgconfig(shout) >= 2.1
BuildRequires:  pkgconfig(soxr) >= 0.1.2
BuildRequires:  pkgconfig(speex) >= 1.0.5
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(theoradec) >= 1.0
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(tiger) >= 0.3.1
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau) >= 0.6
BuildRequires:  pkgconfig(vorbis) >= 1.1
BuildRequires:  pkgconfig(vpx) >= 1.5.0
BuildRequires:  pkgconfig(wayland-client) >= 1.5.91
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.4
BuildRequires:  pkgconfig(wayland-scanner)
#BuildRequires:  pkgconfig(x262)
BuildRequires:  pkgconfig(x264) >= 0.86
#BuildRequires:  pkgconfig(x26410b)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:  pkgconfig(xcb-randr) >= 1.3
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xv) >= 1.1.90.1
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28

%ifarch x86_64
BuildRequires:  pkgconfig(vpl)
%endif

%ifarch armv7hl
BuildRequires:  pkgconfig(mmal)
BuildRequires:  pkgconfig(openmaxil)
%endif

Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
# For xdg-screensaver
Requires:       xdg-utils

Provides:       %{name}-plugin-jack = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-jack < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-cli = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-cli < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-gui-ncurses = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-gui-ncurses < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-gui-qt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-gui-qt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-gui-skins2 = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-gui-skins2 < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-crystalhd = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-crystalhd < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-ffmpeg = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-ffmpeg < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-fluidsynth = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-fluidsynth < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-gnome = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-gnome < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-gstreamer = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-gstreamer < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-ieee1394 = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-ieee1394 < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-jack = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-jack < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-kde = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-kde < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-lua = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-lua < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-notify = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-notify < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-pulseaudio = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-pulseaudio < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-samba = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-samba < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-svg = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-svg < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-visualization = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-visualization < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugin-vnc = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-vnc < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugins-base = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugins-base < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-plugins-video-out = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugins-video-out < %{?epoch:%{epoch}:}%{version}-%{release}

%description
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

touch src/revision.txt

sed -i \
    -e 's/lua5.1/lua-5.1/g' \
    -e 's/luac/luac-5.1/g' \
    configure.ac

%build
# Calls autoreconf to generate m4 macros and prepare Makefiles
./bootstrap
%configure \
    --disable-silent-rules \
    --disable-optimizations \
    --disable-opencv \
    --disable-rpath \
%ifarch armv7hl
	--enable-omxil \
	--enable-omxil-vout \
	--enable-rpi-omxil \
	--enable-mmal \
%endif
    --enable-aa \
    --enable-bpg \
    --enable-daala \
    --enable-fdkaac \
    --enable-lirc \
    --enable-realrtsp \
    --enable-tremor \
    --enable-wayland \
    --with-default-font=%{_datadir}/fonts/dejavu/DejaVuSans.ttf \
    --with-default-font-family=DejaVuSans \
    --with-default-monospace-font=%{_datadir}/fonts/dejavu/DejaVuSansMono.ttf \
    --with-default-monospace-font-family=DejaVuSansMono \
    --with-pic

%make_build

%install
%make_install

find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete

# Remove installed fonts for skins2
rm -fr %{buildroot}%{_datadir}/%{name}/skins2/fonts

# Let the docs section pick up files
rm -fr %{buildroot}%{_docdir}/%{name}

# ?
rm -fr %{buildroot}%{_datadir}/macosx

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/vlc.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%post
%{_libdir}/%{name}/vlc-cache-gen %{_libdir}/%{name} &>/dev/null

%preun
if [ $1 -eq 0 ] ; then
  rm -f %{_libdir}/%{name}/plugins/plugins*.dat &>/dev/null || :
fi

%postun
%{_libdir}/%{name}/vlc-cache-gen %{_libdir}/%{name} &>/dev/null

%posttrans
%{_libdir}/%{name}/vlc-cache-gen %{_libdir}/%{name}/plugins &>/dev/null || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/cvlc
%{_bindir}/nvlc
%{_bindir}/qvlc
%{_bindir}/rvlc
%{_bindir}/svlc
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/*
%{_datadir}/kde4/apps/solid/actions/*
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.xpm
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/*.so.*
%ghost %{_libdir}/%{name}/plugins/plugins.dat
%{_libdir}/%{name}/*.so*
%{_libdir}/%{name}/%{name}-cache-gen
%{_libdir}/%{name}/lua
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/*/
%{_libdir}/%{name}/plugins/access/libaccess_alsa_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_concat_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_imem_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_jack_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_mms_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_mtp_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_realrtsp_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_srt_plugin.so
%{_libdir}/%{name}/plugins/access/libattachment_plugin.so
%{_libdir}/%{name}/plugins/access/libavio_plugin.so
%{_libdir}/%{name}/plugins/access/libcdda_plugin.so
%{_libdir}/%{name}/plugins/access/libdc1394_plugin.so
#%{_libdir}/%{name}/plugins/access/libdecklink_plugin.so
%{_libdir}/%{name}/plugins/access/libdtv_plugin.so
%{_libdir}/%{name}/plugins/access/libdv1394_plugin.so
%{_libdir}/%{name}/plugins/access/libdvb_plugin.so
%{_libdir}/%{name}/plugins/access/libdvdnav_plugin.so
%{_libdir}/%{name}/plugins/access/libdvdread_plugin.so
%{_libdir}/%{name}/plugins/access/libfilesystem_plugin.so
%{_libdir}/%{name}/plugins/access/libftp_plugin.so
%{_libdir}/%{name}/plugins/access/libhttp_plugin.so
%{_libdir}/%{name}/plugins/access/libhttps_plugin.so
%{_libdir}/%{name}/plugins/access/libidummy_plugin.so
%{_libdir}/%{name}/plugins/access/libimem_plugin.so
%{_libdir}/%{name}/plugins/access/liblibbluray_plugin.so
%{_libdir}/%{name}/plugins/access/liblinsys_hdsdi_plugin.so
%{_libdir}/%{name}/plugins/access/liblinsys_sdi_plugin.so
%{_libdir}/%{name}/plugins/access/liblive555_plugin.so
%{_libdir}/%{name}/plugins/access/libnfs_plugin.so
%{_libdir}/%{name}/plugins/access/libpulsesrc_plugin.so
%{_libdir}/%{name}/plugins/access/librist_plugin.so
%{_libdir}/%{name}/plugins/access/librtp_plugin.so
%{_libdir}/%{name}/plugins/access/libsatip_plugin.so
%{_libdir}/%{name}/plugins/access/libsdp_plugin.so
%{_libdir}/%{name}/plugins/access/libsftp_plugin.so
%{_libdir}/%{name}/plugins/access/libshm_plugin.so
%{_libdir}/%{name}/plugins/access/libsmb_plugin.so
%{_libdir}/%{name}/plugins/access/libtcp_plugin.so
%{_libdir}/%{name}/plugins/access/libtimecode_plugin.so
%{_libdir}/%{name}/plugins/access/libudp_plugin.so
%{_libdir}/%{name}/plugins/access/libv4l2_plugin.so
%{_libdir}/%{name}/plugins/access/libvcd_plugin.so
%{_libdir}/%{name}/plugins/access/libvdr_plugin.so
%{_libdir}/%{name}/plugins/access/libvnc_plugin.so
%{_libdir}/%{name}/plugins/access/libxcb_screen_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_dummy_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_file_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_http_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_livehttp_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_rist_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_shout_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_srt_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_udp_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libaudio_format_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libaudiobargraph_a_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libchorus_flanger_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libcompressor_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libdolby_surround_decoder_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libequalizer_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libgain_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libkaraoke_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libmad_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libmono_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libnormvol_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libparam_eq_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libremap_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libsamplerate_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libscaletempo_pitch_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libscaletempo_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libsimple_channel_mixer_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libsoxr_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libspatializer_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libspeex_resampler_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libstereo_widen_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libtospdif_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libtrivial_channel_mixer_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libugly_resampler_plugin.so
%{_libdir}/%{name}/plugins/audio_mixer/libfloat_mixer_plugin.so
%{_libdir}/%{name}/plugins/audio_mixer/libinteger_mixer_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libadummy_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libafile_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libalsa_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libamem_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libjack_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libpulse_plugin.so
%{_libdir}/%{name}/plugins/codec/liba52_plugin.so
%{_libdir}/%{name}/plugins/codec/libadpcm_plugin.so
%{_libdir}/%{name}/plugins/codec/libaes3_plugin.so
%{_libdir}/%{name}/plugins/codec/libaom_plugin.so
%{_libdir}/%{name}/plugins/codec/libaraw_plugin.so
%{_libdir}/%{name}/plugins/codec/libavcodec_plugin.so
%{_libdir}/%{name}/plugins/codec/libcc_plugin.so
%{_libdir}/%{name}/plugins/codec/libcdg_plugin.so
%{_libdir}/%{name}/plugins/codec/libcvdsub_plugin.so
%{_libdir}/%{name}/plugins/codec/libdaala_plugin.so
%{_libdir}/%{name}/plugins/codec/libdav1d_plugin.so
%{_libdir}/%{name}/plugins/codec/libdca_plugin.so
%{_libdir}/%{name}/plugins/codec/libddummy_plugin.so
%{_libdir}/%{name}/plugins/codec/libdvbsub_plugin.so
%{_libdir}/%{name}/plugins/codec/libedummy_plugin.so
%{_libdir}/%{name}/plugins/codec/libfdkaac_plugin.so
%{_libdir}/%{name}/plugins/codec/libflac_plugin.so
%{_libdir}/%{name}/plugins/codec/libfluidsynth_plugin.so
%{_libdir}/%{name}/plugins/codec/libg711_plugin.so
%{_libdir}/%{name}/plugins/codec/libgstdecode_plugin.so
%{_libdir}/%{name}/plugins/codec/libjpeg_plugin.so
%{_libdir}/%{name}/plugins/codec/libkate_plugin.so
%{_libdir}/%{name}/plugins/codec/liblibass_plugin.so
%{_libdir}/%{name}/plugins/codec/liblibmpeg2_plugin.so
%{_libdir}/%{name}/plugins/codec/liblpcm_plugin.so
%{_libdir}/%{name}/plugins/codec/libmpg123_plugin.so
%{_libdir}/%{name}/plugins/codec/liboggspots_plugin.so
%{_libdir}/%{name}/plugins/codec/libopus_plugin.so
%{_libdir}/%{name}/plugins/codec/libpng_plugin.so
%{_libdir}/%{name}/plugins/codec/librawvideo_plugin.so
%{_libdir}/%{name}/plugins/codec/librtpvideo_plugin.so
%{_libdir}/%{name}/plugins/codec/libschroedinger_plugin.so
%{_libdir}/%{name}/plugins/codec/libscte18_plugin.so
%{_libdir}/%{name}/plugins/codec/libscte27_plugin.so
%{_libdir}/%{name}/plugins/codec/libsdl_image_plugin.so
%{_libdir}/%{name}/plugins/codec/libspeex_plugin.so
%{_libdir}/%{name}/plugins/codec/libspdif_plugin.so
%{_libdir}/%{name}/plugins/codec/libspudec_plugin.so
%{_libdir}/%{name}/plugins/codec/libstl_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubsdec_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubstx3g_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubsusf_plugin.so
%{_libdir}/%{name}/plugins/codec/libsvcdsub_plugin.so
%{_libdir}/%{name}/plugins/codec/libsvgdec_plugin.so
%{_libdir}/%{name}/plugins/codec/libt140_plugin.so
%{_libdir}/%{name}/plugins/codec/libtelx_plugin.so
%{_libdir}/%{name}/plugins/codec/libtextst_plugin.so
%{_libdir}/%{name}/plugins/codec/libtheora_plugin.so
%{_libdir}/%{name}/plugins/codec/libttml_plugin.so
%{_libdir}/%{name}/plugins/codec/libtwolame_plugin.so
%{_libdir}/%{name}/plugins/codec/libuleaddvaudio_plugin.so
#%{_libdir}/%{name}/plugins/codec/libvaapi_plugin.so
#%{_libdir}/%{name}/plugins/codec/libvaapi_drm_plugin.so
%{_libdir}/%{name}/plugins/codec/libvorbis_plugin.so
%{_libdir}/%{name}/plugins/codec/libvpx_plugin.so
%{_libdir}/%{name}/plugins/codec/libwebvtt_plugin.so
%{_libdir}/%{name}/plugins/codec/libx264_plugin.so
%{_libdir}/%{name}/plugins/codec/libx26410b_plugin.so
%{_libdir}/%{name}/plugins/codec/libx265_plugin.so
%{_libdir}/%{name}/plugins/codec/libxwd_plugin.so
%{_libdir}/%{name}/plugins/codec/libzvbi_plugin.so
%{_libdir}/%{name}/plugins/control/libdbus_plugin.so
%{_libdir}/%{name}/plugins/control/libdummy_plugin.so
%{_libdir}/%{name}/plugins/control/libgestures_plugin.so
%{_libdir}/%{name}/plugins/control/libhotkeys_plugin.so
%{_libdir}/%{name}/plugins/control/liblirc_plugin.so
%{_libdir}/%{name}/plugins/control/libmotion_plugin.so
%{_libdir}/%{name}/plugins/control/libnetsync_plugin.so
%{_libdir}/%{name}/plugins/control/liboldrc_plugin.so
%{_libdir}/%{name}/plugins/control/libxcb_hotkeys_plugin.so
%{_libdir}/%{name}/plugins/demux/libadaptive_plugin.so
%{_libdir}/%{name}/plugins/demux/libaiff_plugin.so
%{_libdir}/%{name}/plugins/demux/libasf_plugin.so
%{_libdir}/%{name}/plugins/demux/libau_plugin.so
%{_libdir}/%{name}/plugins/demux/libavformat_plugin.so
%{_libdir}/%{name}/plugins/demux/libavi_plugin.so
%{_libdir}/%{name}/plugins/demux/libcaf_plugin.so
%{_libdir}/%{name}/plugins/demux/libdemux_cdg_plugin.so
%{_libdir}/%{name}/plugins/demux/libdemux_chromecast_plugin.so
%{_libdir}/%{name}/plugins/demux/libdirectory_demux_plugin.so
%{_libdir}/%{name}/plugins/demux/libdemux_stl_plugin.so
%{_libdir}/%{name}/plugins/demux/libdemuxdump_plugin.so
%{_libdir}/%{name}/plugins/demux/libdiracsys_plugin.so
%{_libdir}/%{name}/plugins/demux/libes_plugin.so
%{_libdir}/%{name}/plugins/demux/libflacsys_plugin.so
%{_libdir}/%{name}/plugins/demux/libgme_plugin.so
%{_libdir}/%{name}/plugins/demux/libh26x_plugin.so
%{_libdir}/%{name}/plugins/demux/libimage_plugin.so
%{_libdir}/%{name}/plugins/demux/libmjpeg_plugin.so
%{_libdir}/%{name}/plugins/demux/libmkv_plugin.so
%{_libdir}/%{name}/plugins/demux/libmod_plugin.so
%{_libdir}/%{name}/plugins/demux/libmp4_plugin.so
%{_libdir}/%{name}/plugins/demux/libmpc_plugin.so
%{_libdir}/%{name}/plugins/demux/libmpgv_plugin.so
%{_libdir}/%{name}/plugins/demux/libnoseek_plugin.so
%{_libdir}/%{name}/plugins/demux/libnsc_plugin.so
%{_libdir}/%{name}/plugins/demux/libnsv_plugin.so
%{_libdir}/%{name}/plugins/demux/libnuv_plugin.so
%{_libdir}/%{name}/plugins/demux/libogg_plugin.so
%{_libdir}/%{name}/plugins/demux/libplaylist_plugin.so
%{_libdir}/%{name}/plugins/demux/libps_plugin.so
%{_libdir}/%{name}/plugins/demux/libpva_plugin.so
%{_libdir}/%{name}/plugins/demux/librawaud_plugin.so
%{_libdir}/%{name}/plugins/demux/librawdv_plugin.so
%{_libdir}/%{name}/plugins/demux/librawvid_plugin.so
%{_libdir}/%{name}/plugins/demux/libreal_plugin.so
%{_libdir}/%{name}/plugins/demux/libsmf_plugin.so
%{_libdir}/%{name}/plugins/demux/libsubtitle_plugin.so
%{_libdir}/%{name}/plugins/demux/libts_plugin.so
%{_libdir}/%{name}/plugins/demux/libtta_plugin.so
%{_libdir}/%{name}/plugins/demux/libty_plugin.so
%{_libdir}/%{name}/plugins/demux/libvc1_plugin.so
%{_libdir}/%{name}/plugins/demux/libvobsub_plugin.so
%{_libdir}/%{name}/plugins/demux/libvoc_plugin.so
%{_libdir}/%{name}/plugins/demux/libwav_plugin.so
%{_libdir}/%{name}/plugins/demux/libxa_plugin.so
%{_libdir}/%{name}/plugins/gui/libncurses_plugin.so
%{_libdir}/%{name}/plugins/gui/libqt_plugin.so
%{_libdir}/%{name}/plugins/gui/libskins2_plugin.so
%{_libdir}/%{name}/plugins/keystore/libfile_keystore_plugin.so
%{_libdir}/%{name}/plugins/keystore/libkwallet_plugin.so
%{_libdir}/%{name}/plugins/keystore/libmemory_keystore_plugin.so
%{_libdir}/%{name}/plugins/keystore/libsecret_plugin.so
%{_libdir}/%{name}/plugins/logger/libconsole_logger_plugin.so
%{_libdir}/%{name}/plugins/logger/libfile_logger_plugin.so
%{_libdir}/%{name}/plugins/logger/libsd_journal_plugin.so
%{_libdir}/%{name}/plugins/logger/libsyslog_plugin.so
%{_libdir}/%{name}/plugins/lua/liblua_plugin.so
%{_libdir}/%{name}/plugins/meta_engine/libfolder_plugin.so
%{_libdir}/%{name}/plugins/meta_engine/libtaglib_plugin.so
%{_libdir}/%{name}/plugins/misc/libaddonsfsstorage_plugin.so
%{_libdir}/%{name}/plugins/misc/libaddonsvorepository_plugin.so
%{_libdir}/%{name}/plugins/misc/libaudioscrobbler_plugin.so
%{_libdir}/%{name}/plugins/misc/libdbus_screensaver_plugin.so
%{_libdir}/%{name}/plugins/misc/libexport_plugin.so
%{_libdir}/%{name}/plugins/misc/libfingerprinter_plugin.so
%{_libdir}/%{name}/plugins/misc/libgnutls_plugin.so
%{_libdir}/%{name}/plugins/misc/liblogger_plugin.so
%{_libdir}/%{name}/plugins/misc/libstats_plugin.so
%{_libdir}/%{name}/plugins/misc/libvod_rtsp_plugin.so
%{_libdir}/%{name}/plugins/misc/libxdg_screensaver_plugin.so
%{_libdir}/%{name}/plugins/misc/libxml_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_asf_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_avi_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_dummy_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_mp4_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_mpjpeg_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_ogg_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_ps_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_ts_plugin.so
%{_libdir}/%{name}/plugins/mux/libmux_wav_plugin.so
%{_libdir}/%{name}/plugins/notify/libnotify_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_a52_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_av1_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_avparser_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_copy_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_dirac_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_dts_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_flac_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_h264_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_hevc_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mlp_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpegaudio_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_vc1_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libavahi_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libmediadirs_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libmicrodns_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libmtp_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libpodcast_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libpulselist_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libsap_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libudev_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libupnp_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libxcb_apps_plugin.so
%{_libdir}/%{name}/plugins/spu/libaudiobargraph_v_plugin.so
%{_libdir}/%{name}/plugins/spu/libdynamicoverlay_plugin.so
%{_libdir}/%{name}/plugins/spu/liblogo_plugin.so
%{_libdir}/%{name}/plugins/spu/libmarq_plugin.so
%{_libdir}/%{name}/plugins/spu/libmosaic_plugin.so
%{_libdir}/%{name}/plugins/spu/libremoteosd_plugin.so
%{_libdir}/%{name}/plugins/spu/librss_plugin.so
%{_libdir}/%{name}/plugins/spu/libsubsdelay_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libadf_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libaribcam_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libcache_block_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libcache_read_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libdecomp_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libhds_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libinflate_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libprefetch_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/librecord_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libskiptags_plugin.so
%{_libdir}/%{name}/plugins/stream_extractor/libarchive_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_autodel_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_bridge_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_chromaprint_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_chromecast_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_cycle_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_delay_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_description_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_display_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_dummy_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_duplicate_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_es_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_gather_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_record_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_rtp_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_setid_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_smem_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_standard_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_stats_plugin.so
%{_libdir}/%{name}/plugins/stream_out/libstream_out_transcode_plugin.so
%{_libdir}/%{name}/plugins/text_renderer/libfreetype_plugin.so
%{_libdir}/%{name}/plugins/text_renderer/libsvg_plugin.so
%{_libdir}/%{name}/plugins/text_renderer/libtdummy_plugin.so
%{_libdir}/%{name}/plugins/vaapi/libvaapi_filters_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_adjust_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_avcodec_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_chroma_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_deinterlace_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_display_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_sharpen_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libchain_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libgrey_yuv_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_10_p010_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_nv12_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_i420_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/librv32_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libswscale_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuvp_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuy2_i420_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuy2_i422_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libadjust_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libalphamask_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libanaglyph_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libantiflicker_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libball_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libblend_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libblendbench_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libbluescreen_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcanvas_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcolorthres_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcroppadd_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libdeinterlace_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libedgedetection_plugin.so
%{_libdir}/%{name}/plugins/video_filter/liberase_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libextract_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libfps_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libfreeze_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libgaussianblur_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libgradfun_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libgradient_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libgrain_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libhqdn3d_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libinvert_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmagnify_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmirror_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmotionblur_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmotiondetect_plugin.so
%{_libdir}/%{name}/plugins/video_filter/liboldmovie_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libposterize_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpostproc_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpsychedelic_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpuzzle_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libripple_plugin.so
%{_libdir}/%{name}/plugins/video_filter/librotate_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libscale_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libscene_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libsepia_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libsharpen_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libtransform_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libvhs_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libwave_plugin.so
%{_libdir}/%{name}/plugins/video_output/libaa_plugin.so
%{_libdir}/%{name}/plugins/video_output/libcaca_plugin.so
#%{_libdir}/%{name}/plugins/video_output/libdecklinkoutput_plugin.so
%{_libdir}/%{name}/plugins/video_output/libegl_wl_plugin.so
%{_libdir}/%{name}/plugins/video_output/libegl_x11_plugin.so
%{_libdir}/%{name}/plugins/video_output/libfb_plugin.so
%{_libdir}/%{name}/plugins/video_output/libflaschen_plugin.so
%{_libdir}/%{name}/plugins/video_output/libgl_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglconv_vaapi_drm_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglconv_vaapi_wl_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglconv_vaapi_x11_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglconv_vdpau_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglx_plugin.so
%{_libdir}/%{name}/plugins/video_output/libvdummy_plugin.so
%{_libdir}/%{name}/plugins/video_output/libvmem_plugin.so
%{_libdir}/%{name}/plugins/video_output/libwl_shell_plugin.so
%{_libdir}/%{name}/plugins/video_output/libwl_shm_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_x11_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_window_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_xv_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxdg_shell_plugin.so
%{_libdir}/%{name}/plugins/video_output/libyuv_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libclone_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libpanoramix_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libwall_plugin.so
%{_libdir}/%{name}/plugins/visualization/libglspectrum_plugin.so
%{_libdir}/%{name}/plugins/visualization/libprojectm_plugin.so
%{_libdir}/%{name}/plugins/visualization/libvisual_plugin.so

%ifarch armv7hl
%{_libdir}/%{name}/plugins/codec/libomxil_plugin.so
%{_libdir}/%{name}/plugins/codec/libomxil_vout_plugin.so
%endif

%ifarch x86_64
%{_libdir}/%{name}/plugins/codec/libqsv_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_sse2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_sse2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_sse2_plugin.so
%endif

%files devel
%{_includedir}/vlc
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Jun 16 2024 Simone Caronni <negativo17@gmail.com> - 2:3.0.21-2
- Rebuild for updated depdendencies.

* Thu Jun 13 2024 Simone Caronni <negativo17@gmail.com> - 2:3.0.21-1
- Update to 3.0.21.

* Sat Apr 06 2024 Simone Caronni <negativo17@gmail.com> - 2:3.0.20-4
- Clean up SPEC file.
- Switch from Intel MediaSDK to VPL.
- Disable codec/vaapi (leave only video output) as in Fedora to drop ffmpeg4.

* Wed Jan 03 2024 Simone Caronni <negativo17@gmail.com> - 2:3.0.20-3
- Fix typo, main package should not provide devel subpackage.
- Drop Raspberry PI patch and add crypto policies patch.

* Tue Dec 19 2023 Simone Caronni <negativo17@gmail.com> - 2:3.0.20-2
- Update Epoch.
- Obsolete/provide current split packages just introduced in Fedora.

* Thu Nov 23 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.20-1
- Update to 3.0.20.

* Mon Oct 09 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.19-1
- Update to 3.0.19.

* Wed Jun 07 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-6
- Rebuild for updated dependencies.

* Fri Apr 21 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-5
- Disable DCP plugin.

* Thu Mar 16 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-4
- Enable SRT plugin.

* Sun Feb 12 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-3
- Split SPEC file per distribution.

* Thu Jan 05 2023 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-2
- Rebuild for updated dependencies.

* Tue Oct 25 2022 Simone Caronni <negativo17@gmail.com> - 1:3.0.18-1
- Update to 3.0.18.

* Fri Sep 23 2022 Simone Caronni <negativo17@gmail.com> - 1:3.0.17.4-2
- Rebuild for updated dependencies.

* Sat Apr 09 2022 Simone Caronni <negativo17@gmail.com> - 1:3.0.17.4-1
- Update to 3.0.17.4.

* Mon Mar 21 2022 Simone Caronni <negativo17@gmail.com> - 1:3.0.17.3-1
- Update to 3.0.17.3.
- Drop extras and Jack plugin subpackages.

* Sat Mar 12 2022 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-6
- Enable MicroDNS plugin.

* Thu Dec 02 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-5
- Rebuild for updated depdendencies.
- Fix build with recent CentOS/RHEL 8 updates.

* Sun Oct 03 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-4
- Enable Raspberry Pi support only for 32 bit.

* Tue Jul 27 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-3
- Rebuild for updated dependencies.

* Tue Jul 20 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-2
- Rebuild for updated dependencies.

* Sun Jun 20 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.16-1
- Update to 3.0.16.

* Sun May 23 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.14-1
- Update to 3.0.14.

* Sat May 01 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.13-1
- Update to 3.0.13.

* Sat Apr 17 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.12.1-5
- Fix build on Fedora 34.

* Mon Mar 29 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.12.1-4
- Rebuild for updated dependencies.

* Tue Mar 09 2021 Jean-Marc Liger <ligenix@iscp.fr> - 1:3.0.12.1-3
- Fix RHEL/CentOS 8 build.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.12.1-2
- Enable DTS plugin.

* Tue Jan  5 2021 Simone Caronni <negativo17@gmail.com> - 1:3.0.12.1-1
- Update to 3.0.12.1.
- Switch source to Gitlab.
- Fix aarch64 build.

* Sun Dec 06 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11.1-3
- Rebuild for updated dependencies.
- Allow specifying snapshots in the SPEC file.

* Sun Nov 01 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11.1-2
- Add patches to compile with latest QT.
- Use LUA 5.1 on Fedora and RHEL/CentOS 8+.
- Adjust build options for ARM 64.

* Sun Aug 16 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11.1-1
- Update to 3.0.11.1.

* Wed Jul 15 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11-3
- Rebuild for updated dependencies.

* Wed Jul 08 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11-2
- Rebuild for updated dependencies.

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.11-1
- Update to 3.0.11.
- Update SPEC file.
- Disable FreeRDP plugin until FreeRDP 2.x support is available.
- Trim changelog.
- Enable AOM/av1 plugin.

* Sun May 24 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.10-2
- Momentarily disable Decklink plugin.

* Sat May 16 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.10-1
- Update to 3.0.10.

* Fri Apr 24 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.9.2-1
- Update to 3.0.9.2.

* Tue Mar 17 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-6
- Rebuild for updated dependencies.

* Thu Mar 05 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-5
- Disable FAAC Decoder as it creates more problems than anything.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-4
- Rebuild for updated dependencies.

* Mon Oct 21 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-3
- Rebuild for updated dependencies.

* Fri Sep 06 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-2
- Disable FreeRDP plugin on RHEL/CentOS 7, it requires FreeRDP older than 2.0.

* Tue Sep 03 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.8-1
- Update to 3.0.8.

* Sun Jul 07 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.7.1-1
- Update to 3.0.7.1.

* Sun Jun 16 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.7-1
- Update to 3.0.7.

* Mon May 27 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.6-4
- Rebuild for updated dependencies.

* Wed May 01 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.6-3
- Rebuild for updated dependencies.

* Tue Feb 26 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.6-2
- Rebuild for updated dependencies.

* Sat Jan 12 2019 Simone Caronni <negativo17@gmail.com> - 1:3.0.6-1
- Update to 3.0.6.
