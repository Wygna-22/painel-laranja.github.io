import type { LogoProps } from "./types";
import "./Logo.css";

export default function Logo({
  collapsed = false,
}: LogoProps) {
  return (
    <div className="logo">
      <div className="logo__icon">
        🍊
      </div>

      {!collapsed && (
        <div className="logo__content">
          <h1>Painel Laranja</h1>
          <span>Gestão Inteligente</span>
        </div>
      )}
    </div>
  );
}