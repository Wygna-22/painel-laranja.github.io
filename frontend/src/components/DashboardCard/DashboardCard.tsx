import "./DashboardCard.css";
import type { LucideIcon } from "lucide-react";

interface Props{
    title:string;
    value:number|string;
    icon:LucideIcon;
}

export default function DashboardCard({
    title,
    value,
    icon:Icon,
}:Props){

    return(

        <div className="dashboard-card">

            <div>

                <span>{title}</span>

                <h2>{value}</h2>

            </div>

            <Icon size={34}/>

        </div>

    );

}