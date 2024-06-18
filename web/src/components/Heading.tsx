import { ReactElement } from "react"

type FormProps = { title: string }

const Heading = ({ title }: FormProps): ReactElement => {
  return <h1>{title}</h1>
}

export default Heading