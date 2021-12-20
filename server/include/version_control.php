<?php

function deploy($src, $dst, $filenames)
{
    $src_session = ssh2_connect($src);

    // TODO: get ssh credentials from somewhere
    if (ssh2_auth_password($src_session, "username", "password")) {
        $src_sftp = ssh2_sftp($src_session);

        foreach ($filenames as $f) {
            $src_filename = "ssh2.sftp://" . intval($src_sftp) . $f;
            echo fread(fopen($src_filename, "r"), filesize($src_filename));
        }

        return true;
    } else {
        return false;
    }
}
