import { LocaleConfig } from '@/i18n/config'

export const en = {
    local: 'en',
    name: 'English',
    common: {
        action: {
            getSoftware: 'fetch video data',
            getUserProfile: 'fetch user data',
            getVideoModel: 'fetch video data',
            setUserProfile: 'modify user data',
            setVideoModel: 'modify video data',
            uploadFile: 'upload file',
            videoQuery: 'fetch video data',
        },
        hide: 'Hide',
        level: {
            b: 'Beginner',
            i: 'Intermediate',
            e: 'Expert',
            sum: 'Sum',
        },
        mode: {
            std: 'Standard',
            nf: 'No Flag',
            ng: 'No Guessing',
            dg: 'Recursive Chord'
        },
        msg: {
            actionFail: 'Failed to {0}',
            actionSuccess: 'Succeed to {0}',
            agreeTAC: 'Please agree to Terms and Conditions!',
            confirmPasswordFail: 'Passwords do not match!',
            connectionFail: 'Connection Fails!',
            emailCodeSent: 'The email code has been sent. Please check your inbox!',
            emptyEmail: 'Please enter your email!',
            emptyEmailCode: 'Please enter 6-char email code!',
            emptyPassword: 'Please enter your password!',
            emptyUsername: 'Please enter your username!',
            fileTooLarge: 'Maximum file size is {0}',
            invalidEmail: 'Invalid email!',
            invalidEmailCode: 'Email code is invalid! Please re-sent your email code.',
            invalidPassword: 'The length of password should be from 6 to 20!。',
            invalidUsername: 'The length of username cannot exceed 20!',
            logoutFail: 'Failed to log out!',
            logoutSuccess: 'Log out success!',
            realNameRequired: 'Real name required',
        },
        prop: {
            action: 'Action',
            designator: 'Designator',
            fileName: 'File name',
            is: 'Island',
            level: 'Level',
            op: 'Opening',
            realName: 'Real Name',
            sex: 'Sex',
            status: 'Status',
            time: 'Time',
            timems: 'Time',
            upload_time: 'Upload time',
        },
        response: {
            OK: '',
            BadRequest: 'Unrecognised request',
            Forbidden: 'Permission denied',
            InternalServerError: 'Internal server error',
            NotFound: 'Data not found',
            PayloadTooLarge: 'Payload too large',
            TooManyRequests: 'Too many requests',
            UnsupportedMediaType: 'Unsupported file type',
        },
        show: 'Show',
        software: {
            metasweeper: 'MetaSweeper',
        },
        toDo: 'TODO',
    },
    designatorManager: {
        addDesignatorSuccess: 'Designator Added',
        conflict: 'Designator Conflict',
        delDesignatorSuccess: 'Designator Deleted',
        processedNVideos: '{0} videos have been processed',
        ownedBy: 'The designator is owned by user#{0}',
        notFound: 'You do not have any video of the designator',
    },
    footer: {
        contact: 'Contact',
        donate: 'Donate',
        team: 'Team',
        links: 'LInks',
        about: 'About',
    },
    forgetPassword: {
        title: 'Reset password',
        captcha: 'captcha',
        confirm: 'Reset',
        confirmPassword: 'confirm password',
        email: 'email',
        emailCode: 'one-time password',
        getEmailCode: 'Send one-time password',
        password: 'new password',
        success: 'Password reset complete!'
    },
    guide: {
        announcement: 'Announcements',
        other: 'Others',
        skill: 'Skills',
        tutorial: 'Tutorials',
    },
    home: {
        news: 'News',
        latestScore: 'Latest',
        reviewQueue: 'Pending',
    },
    login: {
        title: 'Login',
        username: 'username',
        password: 'password',
        captcha: 'captcha',
        forgetPassword: 'Forget password?',
        keepMeLoggedIn: 'Keep me logged in',
        confirm: 'Log in'
    },
    menu: {
        ranking: 'Ranking',
        video: 'Videos',
        world: 'Statistics',
        guide: 'Guides',
        score: 'Scores',
        profile: 'Profile',
        welcome: `Welcome, {0}!`,
        login: 'Login',
        logout: 'Logout',
        register: 'Register',
        setting: 'Settings',
    },
    news: {
        breakRecordTo: ' breaks their {mode} {level} {stat} record with ',
    },
    profile: {
        changeAvatar: 'Click the image to change avatar',
        realname: 'Name: ',
        realnameInput: 'Input your real name here',
        signature: 'Bio: ',
        signatureInput: 'Input your bio here',
        change: 'Edit profile',
        confirmChange: 'Confirm',
        cancelChange: 'Cancel',
        designator: 'My designators: ',
        msg: {
            avatarChange: 'Avatar change complete! {0} times left',
            avatarFormat: 'Avatar file has to be in JPG or PNG format!',
            avatarFilesize: 'Maximum file size is 50MB!',
            realnameChange: 'Real name change complete! {0} times left',
            signatureChange: 'Signature change complete! {0} times left',
        },
        records: {
            title: 'Personal Records',
            modeRecord: ' mode record: '
        },
        videos: 'All videos',
        upload: {
            title: 'Video Upload',
            dragOrClick: `Drag files here or <em>click here to select</em>`,
            uploadAll: 'Upload All ({0})',
            cancelAll: 'Clear All',
            constraintNote: '*File size maximum is 5MB.',
            error: {
                collision: 'Video already exist',
                custom: 'Custom level is currently not supported',
                designator: 'Designator mismatch',
                fail: 'Fail',
                fileext: 'Invalid file extension',
                filename: 'File name exceeds 100 bytes',
                filesize: 'File size exceeds 5MB',
                pass: 'Pass',
                process: 'Uploading',
                upload: 'Upload fail',
            }
        }
    },
    register: {
        title: 'Register',
        username: 'username',
        email: 'email',
        captcha: 'captcha',
        getEmailCode: 'Send email code',
        emailCode: 'email code',
        password: 'password',
        confirmPassword: 'confirm password',
        agreeTo: 'Agree to ',
        termsAndConditions: 'Terms & Conditions',
        confirm: 'Register',
    },
    setting: {
        appearance: 'Appearance',
        colorscheme: {
            auto: 'auto',
            dark: 'dark',
            light: 'light',
            title: 'Color scheme',
        },
        languageSwitch: 'Language Switch',
        menuFontSize: 'Menu Font Size',
        menuHeight: 'Menu Height',
        menuLayout: 'Menu Layout',
        menuLayoutAbstract: 'Abstract',
        menuLayoutDefault: 'Default',
    },
    team: {
        title: 'Team',
        owner: 'Owner',
        moderator: 'Moderators',
        software: 'Developers',
        localization: 'Localization',
        zhCn: 'Simplified Chinese',
        en: 'English',
        de: 'German',
        pl: 'Polish',
        designer: 'UI designers',
        acknowledgement: 'Acknowledgement',
    },
}