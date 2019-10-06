/****************************************************************************
**
** Copyright (C) 2017 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the Qt Quick Controls 2 module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.11
import QtQuick.Templates 2.4 as T
import QtQuick.Controls.Imagine 2.4
import QtQuick.Controls.Imagine.impl 2.4

T.StackView {
    id: control

    implicitWidth: background ? background.implicitWidth : 0
    implicitHeight: background ? background.implicitHeight : 0

    topPadding: background ? background.topPadding : 0
    leftPadding: background ? background.leftPadding : 0
    rightPadding: background ? background.rightPadding : 0
    bottomPadding: background ? background.bottomPadding : 0

    popEnter: Transition {
        XAnimator { from: (control.mirrored ? -1 : 1) * -control.width; to: 0; duration: 400; easing.type: Easing.OutCubic }
    }

    popExit: Transition {
        XAnimator { from: 0; to: (control.mirrored ? -1 : 1) * control.width; duration: 400; easing.type: Easing.OutCubic }
    }

    pushEnter: Transition {
        XAnimator { from: (control.mirrored ? -1 : 1) * control.width; to: 0; duration: 400; easing.type: Easing.OutCubic }
    }

    pushExit: Transition {
        XAnimator { from: 0; to: (control.mirrored ? -1 : 1) * -control.width; duration: 400; easing.type: Easing.OutCubic }
    }

    replaceEnter: Transition {
        XAnimator { from: (control.mirrored ? -1 : 1) * control.width; to: 0; duration: 400; easing.type: Easing.OutCubic }
    }

    replaceExit: Transition {
        XAnimator { from: 0; to: (control.mirrored ? -1 : 1) * -control.width; duration: 400; easing.type: Easing.OutCubic }
    }

    background: NinePatchImage {
        x: -leftInset; y: -topInset
        width: control.width + leftInset + rightInset
        height: control.height + topInset + bottomInset

        source: Imagine.url + "stackview-background"
        NinePatchImageSelector on source {
            states: [
                {"disabled": !control.enabled},
                {"mirrored": control.mirrored}
            ]
        }
    }
}
