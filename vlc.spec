%global commit0 6cb361c1fb83c026cb9303db65e27d95b3d077cc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:    The cross-platform open-source multimedia framework, player and server
Name:       vlc
Version:    3.0.0
Release:    2.%{?shortcommit0}%{?dist}
Epoch:      1
License:    GPLv2+
URL:        http://www.videolan.org

#Source0:    http://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
Source0:    %{name}-%{version}-%{shortcommit0}.tar.xz
Source1:    %{name}-snapshot.sh

BuildRequires:  a52dec-devel
BuildRequires:  aalib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  faad2-devel
BuildRequires:  gettext-devel
#BuildRequires:  hostname
BuildRequires:  kdelibs
BuildRequires:  libdvbpsi-devel
BuildRequires:  libebml-devel >= 1.0.0
BuildRequires:  libgcrypt-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmad-devel
#BuildRequires:  libmmal-devel
BuildRequires:  libmatroska-devel >= 1.0.0
BuildRequires:  libmpcdec-devel
BuildRequires:  libtar-devel
BuildRequires:  libtool
BuildRequires:  lirc-devel
BuildRequires:  live555-devel
BuildRequires:  yasm

BuildRequires:  pkgconfig(avahi-client) >= 0.6
BuildRequires:  pkgconfig(alsa) >= 1.0.24
#BuildRequires:  pkgconfig(asdcplib)
BuildRequires:  pkgconfig(caca) >= 0.99.beta14
BuildRequires:  pkgconfig(cairo) >= 1.13.1
BuildRequires:  pkgconfig(dbus-1) >= 1.6.0
BuildRequires:  pkgconfig(dvdnav) > 4.9.0
BuildRequires:  pkgconfig(dvdread) > 4.9.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth) >= 1.1.2
#BuildRequires:  pkgconfig(freerdp) >= 1.0.1
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gnutls) >= 3.0.20
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(jack) >= 1.9.7
BuildRequires:  pkgconfig(libass) >= 0.9.8
BuildRequires:  pkgconfig(libavc1394) >= 0.5.3
BuildRequires:  pkgconfig(libavcodec) >= 53.34.0
BuildRequires:  pkgconfig(libavformat) >= 53.21.0
BuildRequires:  pkgconfig(libavutil) >= 51.22.0
BuildRequires:  pkgconfig(libbluray) >= 0.3.0
BuildRequires:  pkgconfig(libcddb) >= 0.9.5
BuildRequires:  pkgconfig(libchromaprint) >= 0.6.0
BuildRequires:  pkgconfig(libdc1394-2) >= 2.1.0
BuildRequires:  pkgconfig(libidn)
#BuildRequires:  pkgconfig(libgoom2)
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libmodplug) > 0.8.8
BuildRequires:  pkgconfig(libmpeg2) > 0.3.2
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libmtp) >= 1.0.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(libpulse) >= 1.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.1
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.9.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
#BuildRequires:  pkgconfig(libsidplay2)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libudev) >= 142
BuildRequires:  pkgconfig(libupnp)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvncclient) >= 0.9.9
#BuildRequires:  pkgconfig(libvsxu)
BuildRequires:  pkgconfig(lua) >= 5.1
BuildRequires:  pkgconfig(opencv) >= 2.0
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(opus) >= 1.0.3
BuildRequires:  pkgconfig(protobuf-lite) >= 2.5.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:  pkgconfig(sdl) >= 1.2.10
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(SDL_image) >= 1.2.10
#BuildRequires:  pkgconfig(shine) >= 3.0.0
BuildRequires:  pkgconfig(shout) >= 2.1
BuildRequires:  pkgconfig(speex) >= 1.0.5
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(theoradec) >= 1.0
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(tiger) >= 0.3.1
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau) >= 0.6
BuildRequires:  pkgconfig(vorbis) >= 1.1
BuildRequires:  pkgconfig(vpx)
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

Requires:       vlc-core%{_isa} = %{?epoch}:%{version}-%{release}
Requires:       kde-filesystem

Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts

# For xdg-screensaver
Requires:       xdg-utils

%description
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-core%{_isa} = %{?epoch}:%{version}-%{release}

%description devel
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package core
Summary:        VLC media player core

%description core
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

This package contains the core components.

%package extras
Summary:        VLC media player with extras modules
Requires:       vlc-core%{_isa} = %{?epoch}:%{version}-%{release}


%description extras
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

This package contains the extra modules.

%package plugin-jack
Summary:        JACK audio plugin for VLC
Requires:       vlc-core%{_isa} = %{?epoch}:%{version}-%{release}

%description plugin-jack
VLC is a free and open source cross-platform multimedia player and framework
that plays most multimedia files as well as DVDs, Audio CDs, VCDs, and various
streaming protocols.

This package contains the JACK audio plugin.


%prep
%setup -q -n %{name}

%build
# Calls autoreconf to generate m4 macros and prepare Makefiles
./bootstrap
%configure \
    --disable-silent-rules \
    --disable-optimizations \
    --disable-rpath \
    --enable-aa \
    --enable-fdkaac \
    --enable-lirc \
    --enable-omxil \
    --with-default-font=%{_datadir}/fonts/dejavu/DejaVuSans.ttf \
    --with-default-font-family=DejaVuSans \
    --with-default-monospace-font=%{_datadir}/fonts/dejavu/DejaVuSansMono.ttf \
    --with-default-monospace-font-family=DejaVuSansMono \
    --with-pic

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p" CPPROG="cp -p"

find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete

desktop-file-validate %{buildroot}%{_datadir}/applications/vlc.desktop

# Remove installed fonts for skins2
rm -fr %{buildroot}%{_datadir}/%{name}/skins2/fonts

# Let the docs section pick up files
rm -fr %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%post
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name} &>/dev/null
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/update-desktop-database &> /dev/null || :

%postun
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name} &>/dev/null
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%post core -p /sbin/ldconfig

%postun core -p /sbin/ldconfig

%posttrans core
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name}/plugins &>/dev/null || :

%post extras
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name}/plugins &>/dev/null || :

%postun extras
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name}/plugins &>/dev/null || :

%post plugin-jack
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name}/plugins &>/dev/null || :

%postun plugin-jack
%{_libdir}/%{name}/vlc-cache-gen -f %{_libdir}/%{name}/plugins &>/dev/null || :

%preun core
if [ $1 -eq 0 ] ; then
  rm -f %{_libdir}/%{name}/plugins/plugins*.dat &>/dev/null || :
fi

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/qvlc
%{_bindir}/svlc
%{_datadir}/applications/*
%{_datadir}/kde4/apps/solid/actions/*
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/hicolor/*/apps/%{name}*.xpm
%{_datadir}/%{name}/skins2
%{_libdir}/%{name}/plugins/access/libxcb_screen_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libpulse_plugin.so
%{_libdir}/%{name}/plugins/gui/libqt_plugin.so
%{_libdir}/%{name}/plugins/gui/libskins2_plugin.so
%{_libdir}/%{name}/plugins/video_output/libaa_plugin.so
%{_libdir}/%{name}/plugins/video_output/libcaca_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_glx_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_x11_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_window_plugin.so
%{_libdir}/%{name}/plugins/video_output/libxcb_xv_plugin.so
%{_libdir}/%{name}/plugins/visualization/libprojectm_plugin.so

%files core -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/cvlc
%{_bindir}/nvlc
%{_bindir}/rvlc
%{_bindir}/%{name}-wrapper
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/lua
%{_datadir}/%{name}/utils
%{_datadir}/%{name}/%{name}.ico
%ghost %{_libdir}/%{name}/plugins/plugins.dat
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/access
%dir %{_libdir}/%{name}/plugins/access_output
%dir %{_libdir}/%{name}/plugins/audio_filter
%dir %{_libdir}/%{name}/plugins/audio_mixer
%dir %{_libdir}/%{name}/plugins/audio_output
%dir %{_libdir}/%{name}/plugins/codec
%dir %{_libdir}/%{name}/plugins/control
%dir %{_libdir}/%{name}/plugins/demux
%dir %{_libdir}/%{name}/plugins/gui
%dir %{_libdir}/%{name}/plugins/keystore
%dir %{_libdir}/%{name}/plugins/logger
%dir %{_libdir}/%{name}/plugins/lua
%dir %{_libdir}/%{name}/plugins/meta_engine
%dir %{_libdir}/%{name}/plugins/misc
%dir %{_libdir}/%{name}/plugins/mux
%dir %{_libdir}/%{name}/plugins/notify
%dir %{_libdir}/%{name}/plugins/packetizer
%dir %{_libdir}/%{name}/plugins/services_discovery
%dir %{_libdir}/%{name}/plugins/stream_filter
%dir %{_libdir}/%{name}/plugins/stream_out
%dir %{_libdir}/%{name}/plugins/text_renderer
%dir %{_libdir}/%{name}/plugins/vdpau
%dir %{_libdir}/%{name}/plugins/video_chroma
%dir %{_libdir}/%{name}/plugins/video_filter
%dir %{_libdir}/%{name}/plugins/video_output
%dir %{_libdir}/%{name}/plugins/video_splitter
%dir %{_libdir}/%{name}/plugins/visualization
%{_libdir}/*.so.*
%{_libdir}/%{name}/*.so*
%{_libdir}/%{name}/lua
%{_libdir}/%{name}/plugins/access/libaccess_alsa_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_bd_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_concat_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_imem_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_mms_plugin.so
%{_libdir}/%{name}/plugins/access/libaccess_mtp_plugin.so
%{_libdir}/%{name}/plugins/access/libattachment_plugin.so
%{_libdir}/%{name}/plugins/access/libavio_plugin.so
%{_libdir}/%{name}/plugins/access/libcdda_plugin.so
%{_libdir}/%{name}/plugins/access/libdc1394_plugin.so
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
%{_libdir}/%{name}/plugins/access/libpulsesrc_plugin.so
%{_libdir}/%{name}/plugins/access/librar_plugin.so
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
%{_libdir}/%{name}/plugins/access/libvdr_plugin.so
%{_libdir}/%{name}/plugins/access/libvnc_plugin.so
%{_libdir}/%{name}/plugins/access/libwl_screenshooter_plugin.so
%{_libdir}/%{name}/plugins/access/libzip_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_dummy_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_file_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_http_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_livehttp_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_shout_plugin.so
%{_libdir}/%{name}/plugins/access_output/libaccess_output_udp_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/liba52tofloat32_plugin.so
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
%{_libdir}/%{name}/plugins/audio_filter/libscaletempo_plugin.so
%{_libdir}/%{name}/plugins/audio_filter/libsimple_channel_mixer_plugin.so
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
%{_libdir}/%{name}/plugins/codec/liba52_plugin.so
%{_libdir}/%{name}/plugins/codec/libadpcm_plugin.so
%{_libdir}/%{name}/plugins/codec/libaes3_plugin.so
%{_libdir}/%{name}/plugins/codec/libaraw_plugin.so
%{_libdir}/%{name}/plugins/codec/libavcodec_plugin.so
%{_libdir}/%{name}/plugins/codec/libcc_plugin.so
%{_libdir}/%{name}/plugins/codec/libcdg_plugin.so
%{_libdir}/%{name}/plugins/codec/libcvdsub_plugin.so
%{_libdir}/%{name}/plugins/codec/libddummy_plugin.so
%{_libdir}/%{name}/plugins/codec/libdts_plugin.so
%{_libdir}/%{name}/plugins/codec/libdvbsub_plugin.so
%{_libdir}/%{name}/plugins/codec/libedummy_plugin.so
%{_libdir}/%{name}/plugins/codec/libfaad_plugin.so
%{_libdir}/%{name}/plugins/codec/libfdkaac_plugin.so
%{_libdir}/%{name}/plugins/codec/libflac_plugin.so
%{_libdir}/%{name}/plugins/codec/libg711_plugin.so
%{_libdir}/%{name}/plugins/codec/libgstdecode_plugin.so
%{_libdir}/%{name}/plugins/codec/libjpeg_plugin.so
%{_libdir}/%{name}/plugins/codec/libkate_plugin.so
%{_libdir}/%{name}/plugins/codec/liblibass_plugin.so
%{_libdir}/%{name}/plugins/codec/liblibmpeg2_plugin.so
%{_libdir}/%{name}/plugins/codec/liblpcm_plugin.so
%{_libdir}/%{name}/plugins/codec/libmpeg_audio_plugin.so
%{_libdir}/%{name}/plugins/codec/libmpg123_plugin.so
%{_libdir}/%{name}/plugins/codec/liboggspots_plugin.so
%{_libdir}/%{name}/plugins/codec/libomxil_plugin.so
%{_libdir}/%{name}/plugins/codec/libopus_plugin.so
%{_libdir}/%{name}/plugins/codec/libpng_plugin.so
%{_libdir}/%{name}/plugins/codec/libqsv_plugin.so
%{_libdir}/%{name}/plugins/codec/librawvideo_plugin.so
%{_libdir}/%{name}/plugins/codec/librtpvideo_plugin.so
%{_libdir}/%{name}/plugins/codec/libschroedinger_plugin.so
%{_libdir}/%{name}/plugins/codec/libscte18_plugin.so
%{_libdir}/%{name}/plugins/codec/libscte27_plugin.so
%{_libdir}/%{name}/plugins/codec/libsdl_image_plugin.so
%{_libdir}/%{name}/plugins/codec/libspeex_plugin.so
%{_libdir}/%{name}/plugins/codec/libspudec_plugin.so
%{_libdir}/%{name}/plugins/codec/libstl_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubsdec_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubsttml_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubstx3g_plugin.so
%{_libdir}/%{name}/plugins/codec/libsubsusf_plugin.so
%{_libdir}/%{name}/plugins/codec/libsvgdec_plugin.so
%{_libdir}/%{name}/plugins/codec/libt140_plugin.so
%{_libdir}/%{name}/plugins/codec/libtelx_plugin.so
%{_libdir}/%{name}/plugins/codec/libtheora_plugin.so
%{_libdir}/%{name}/plugins/codec/libtwolame_plugin.so
%{_libdir}/%{name}/plugins/codec/libuleaddvaudio_plugin.so
%{_libdir}/%{name}/plugins/codec/libvaapi_drm_plugin.so
%{_libdir}/%{name}/plugins/codec/libvaapi_x11_plugin.so
%{_libdir}/%{name}/plugins/codec/libvorbis_plugin.so
%{_libdir}/%{name}/plugins/codec/libvpx_plugin.so
%{_libdir}/%{name}/plugins/codec/libx264_plugin.so
%{_libdir}/%{name}/plugins/codec/libx265_plugin.so
%{_libdir}/%{name}/plugins/codec/libxwd_plugin.so
%{_libdir}/%{name}/plugins/codec/libzvbi_plugin.so
%{_libdir}/%{name}/plugins/control/libdbus_plugin.so
%{_libdir}/%{name}/plugins/control/libdummy_plugin.so
%{_libdir}/%{name}/plugins/control/libgestures_plugin.so
%{_libdir}/%{name}/plugins/control/libhotkeys_plugin.so
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
%{_libdir}/%{name}/plugins/demux/libdemux_stl_plugin.so
%{_libdir}/%{name}/plugins/demux/libdemuxdump_plugin.so
%{_libdir}/%{name}/plugins/demux/libdiracsys_plugin.so
%{_libdir}/%{name}/plugins/demux/libes_plugin.so
%{_libdir}/%{name}/plugins/demux/libflacsys_plugin.so
%{_libdir}/%{name}/plugins/demux/libh26x_plugin.so
%{_libdir}/%{name}/plugins/demux/libimage_plugin.so
%{_libdir}/%{name}/plugins/demux/libmjpeg_plugin.so
%{_libdir}/%{name}/plugins/demux/libmkv_plugin.so
%{_libdir}/%{name}/plugins/demux/libmod_plugin.so
%{_libdir}/%{name}/plugins/demux/libmp4_plugin.so
%{_libdir}/%{name}/plugins/demux/libmpc_plugin.so
%{_libdir}/%{name}/plugins/demux/libmpgv_plugin.so
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
%{_libdir}/%{name}/plugins/demux/libttml_plugin.so
%{_libdir}/%{name}/plugins/demux/libty_plugin.so
%{_libdir}/%{name}/plugins/demux/libvc1_plugin.so
%{_libdir}/%{name}/plugins/demux/libvobsub_plugin.so
%{_libdir}/%{name}/plugins/demux/libvoc_plugin.so
%{_libdir}/%{name}/plugins/demux/libwav_plugin.so
%{_libdir}/%{name}/plugins/demux/libxa_plugin.so
%{_libdir}/%{name}/plugins/gui/libncurses_plugin.so
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
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_avparser_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_copy_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_dirac_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_flac_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_h264_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_hevc_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mlp_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
%{_libdir}/%{name}/plugins/packetizer/libpacketizer_vc1_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libavahi_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libmediadirs_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libmtp_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libpodcast_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libpulselist_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libsap_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libudev_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libupnp_plugin.so
%{_libdir}/%{name}/plugins/services_discovery/libxcb_apps_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libcache_block_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libcache_read_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libdecomp_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libhds_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libinflate_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/libprefetch_plugin.so
%{_libdir}/%{name}/plugins/stream_filter/librecord_plugin.so
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
%{_libdir}/%{name}/plugins/stream_out/libstream_out_raop_plugin.so
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
%{_libdir}/%{name}/plugins/vdpau/libvdpau_adjust_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_avcodec_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_chroma_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_deinterlace_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_display_plugin.so
%{_libdir}/%{name}/plugins/vdpau/libvdpau_sharpen_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libchain_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libgrey_yuv_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_nv12_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_rgb_sse2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi420_yuy2_sse2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_i420_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_mmx_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libi422_yuy2_sse2_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/librv32_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libswscale_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuvp_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuy2_i420_plugin.so
%{_libdir}/%{name}/plugins/video_chroma/libyuy2_i422_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libadjust_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libalphamask_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libanaglyph_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libantiflicker_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libaudiobargraph_v_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libball_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libblend_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libblendbench_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libbluescreen_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcanvas_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcolorthres_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libcroppadd_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libdeinterlace_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libdynamicoverlay_plugin.so
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
%{_libdir}/%{name}/plugins/video_filter/liblogo_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmagnify_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmarq_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmirror_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmosaic_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmotionblur_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libmotiondetect_plugin.so
%{_libdir}/%{name}/plugins/video_filter/liboldmovie_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libposterize_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpostproc_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpsychedelic_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libpuzzle_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libremoteosd_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libripple_plugin.so
%{_libdir}/%{name}/plugins/video_filter/librotate_plugin.so
%{_libdir}/%{name}/plugins/video_filter/librss_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libscale_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libscene_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libsepia_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libsharpen_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libsubsdelay_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libtransform_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libvhs_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libwave_plugin.so
%{_libdir}/%{name}/plugins/video_output/libegl_x11_plugin.so
%{_libdir}/%{name}/plugins/video_output/libfb_plugin.so
%{_libdir}/%{name}/plugins/video_output/libgl_plugin.so
%{_libdir}/%{name}/plugins/video_output/libglx_plugin.so
%{_libdir}/%{name}/plugins/video_output/libvdummy_plugin.so
%{_libdir}/%{name}/plugins/video_output/libvmem_plugin.so
%{_libdir}/%{name}/plugins/video_output/libvout_sdl_plugin.so
%{_libdir}/%{name}/plugins/video_output/libwl_shell_surface_plugin.so
%{_libdir}/%{name}/plugins/video_output/libwl_shm_plugin.so
%{_libdir}/%{name}/plugins/video_output/libyuv_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libclone_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libpanoramix_plugin.so
%{_libdir}/%{name}/plugins/video_splitter/libwall_plugin.so
%{_libdir}/%{name}/plugins/visualization/libglspectrum_plugin.so
%{_libdir}/%{name}/plugins/visualization/libvisual_plugin.so
%{_libdir}/%{name}/%{name}-cache-gen
%{_mandir}/man1/%{name}*.1*

%files plugin-jack
%{_libdir}/%{name}/plugins/access/libaccess_jack_plugin.so
%{_libdir}/%{name}/plugins/audio_output/libjack_plugin.so

%files extras
%{_libdir}/%{name}/plugins/access/libvcd_plugin.so
%{_libdir}/%{name}/plugins/codec/libfluidsynth_plugin.so
%{_libdir}/%{name}/plugins/codec/libsvcdsub_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libopencv_example_plugin.so
%{_libdir}/%{name}/plugins/video_filter/libopencv_wrapper_plugin.so

%files devel
%dir %{_includedir}/vlc
%{_includedir}/vlc/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/vlc-plugin.pc
%{_libdir}/pkgconfig/libvlc.pc

%changelog
* Thu Jul 14 2016 Simone Caronni <negativo17@gmail.com> - 1:3.0.0-2.6cb361c
- Update to latest snapshot.
- Enable libmpeg2, libsecret and protobuf-lite (Chromecast) plugin.

* Tue May 24 2016 Simone Caronni <negativo17@gmail.com> - 1:3.0.0-1.b016524
- Update to a 3.0.0 snapshot.
- Remove Gnome VFS, rdp and libmpeg2 support.
- Enable QT 5.5 interface.
- Enable Wayland output.
- Disable RDP support until FreeRDP decides to make a release and VLC does
  support it.

* Wed Apr 20 2016 Simone Caronni <negativo17@gmail.com> - 1:2.2.2-5
- Rebuild for libprojectM bump.

* Mon Apr 04 2016 Simone Caronni <negativo17@gmail.com> - 1:2.2.2-4
- Rebuild for libva bump.

* Fri Mar 18 2016 Simone Caronni <negativo17@gmail.com> - 1:2.2.2-3
- Fix Matroska build.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 1:2.2.2-2
- Lower gettext requirements for RHEL/CentOS 7.

* Sat Jan 30 2016 Simone Caronni <negativo17@gmail.com> - 1:2.2.2-1
- First build.
