<?php

function deploy($src, $dst, $add, $rm)
{
    $src_session = ssh2_connect($src);
    $dst_session = ssh2_connect($dst);

    // TODO: get ssh credentials from somewhere
    if (
        ssh2_auth_password($src_session, "username", "password") &&
        ssh2_auth_password($dst_session, "username", "password")
    ) {
        $src_sftp = ssh2_sftp($src_session);
        $dst_sftp = ssh2_sftp($dst_session);

        foreach ($add as $f) {
            $src_fn = "ssh2.sftp://" . intval($src_sftp) . $f;
            $dst_fn = "ssh2.sftp://" . intval($dst_sftp) . $f;

            fwrite(
                fopen($dst_fn, "w"),
                fread(fopen($src_fn, "r"), filesize($src_fn))
            );
        }

        foreach ($rm as $f) {
            ssh2_sftp_unlink($dst_sftp, $f);
        }

        return true;
    } else {
        return false;
    }
}
