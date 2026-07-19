import "./Button.css";

import type { ButtonProps } from "./types";

export default function Button({

    children,

    variant = "primary",

    fullWidth = false,

    loading = false,

    className = "",

    disabled,

    ...props

}: ButtonProps){

    return(

        <button

            className={`
                button
                button--${variant}
                ${fullWidth ? "button--full" : ""}
                ${className}
            `}

            disabled={disabled || loading}

            {...props}

        >

            {loading ? "Carregando..." : children}

        </button>

    )

}